// Replace this after `sam deploy --guided`, e.g. https://abc.execute-api.ap-south-1.amazonaws.com/Prod
const API_URL = "PASTE_YOUR_API_GATEWAY_URL_HERE";

const input = document.querySelector('#fileInput'), dropzone = document.querySelector('#dropzone');
const selected = document.querySelector('#selected'), fileName = document.querySelector('#fileName');
const analyse = document.querySelector('#analyse'), message = document.querySelector('#message'), results = document.querySelector('#results');
let file;
function setMessage(text) { message.textContent = text; }
function choose(candidate) { if (!candidate || candidate.type !== 'application/pdf') return setMessage('Please choose a PDF file.'); file=candidate; fileName.textContent=file.name; selected.hidden=false; analyse.disabled=false; setMessage('Ready to analyze.'); }
input.addEventListener('change', () => choose(input.files[0]));
['dragenter','dragover'].forEach(e=>dropzone.addEventListener(e,e=>{e.preventDefault();dropzone.classList.add('active')}));
['dragleave','drop'].forEach(e=>dropzone.addEventListener(e,e=>{e.preventDefault();dropzone.classList.remove('active')}));
dropzone.addEventListener('drop',e=>choose(e.dataTransfer.files[0]));
document.querySelector('#clearFile').onclick=()=>{file=null; input.value=''; selected.hidden=true; analyse.disabled=true;results.hidden=true;setMessage('')};
async function json(url, options) { const r=await fetch(url,options); const data=await r.json(); if(!r.ok) throw Error(data.message||'Request failed'); return data; }
async function poll(id) { for(let n=0;n<40;n++){ await new Promise(r=>setTimeout(r,3000)); const state=await json(`${API_URL}/result/${id}`); if(state.status==='COMPLETE') return state.result; if(state.status==='FAILED') throw Error(state.message||'The document could not be processed.'); setMessage(`Reading document… (${(n+1)*3}s)`); } throw Error('Analysis is taking longer than expected. Try again shortly.'); }
function render(result){results.innerHTML='';const heading=document.createElement('div');heading.className='result-heading';heading.innerHTML=`<h2>Your action plan</h2><p>${result.summary||'Key details extracted from your document.'}</p>`;results.append(heading);const groups=[['Deadlines',result.deadlines],['Eligibility',result.eligibility],['Required documents',result.requiredDocuments],['Next steps',result.nextSteps],['Important warnings',result.importantWarnings]];for(const [title,items] of groups){if(!items?.length)continue;const node=document.querySelector('#listTemplate').content.cloneNode(true);node.querySelector('h2').textContent=title;node.querySelector('ul').innerHTML=items.map(v=>`<li>${escapeHtml(v)}</li>`).join('');results.append(node)}results.hidden=false;results.scrollIntoView({behavior:'smooth'})}
function escapeHtml(s){const d=document.createElement('div');d.textContent=s;return d.innerHTML}
analyse.onclick=async()=>{if(!file)return;if(API_URL.includes('PASTE_YOUR'))return setMessage('Add your API Gateway URL in script.js first.');analyse.disabled=true;results.hidden=true;try{setMessage('Creating a secure upload…');const up=await json(`${API_URL}/upload-url`,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({fileName:file.name,contentType:file.type})});setMessage('Uploading securely…');const put=await fetch(up.uploadUrl,{method:'PUT',headers:{'Content-Type':'application/pdf'},body:file});if(!put.ok)throw Error('Upload failed.');setMessage('Starting AI analysis…');await json(`${API_URL}/process`,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({documentId:up.documentId})});render(await poll(up.documentId));setMessage('Analysis complete.')}catch(e){setMessage(e.message)}finally{analyse.disabled=false}};
