// 하위 요소를 모두 제거해주는 함수 
// 드래그앤 드롭 하나만 들어오게 막아 주기 위해 생성 
function deleteChilds(target){
  while (target.hasChildNodes()){
    target.removeChild( target.firstChild );       
  } 
}

function DropFile(dropAreaId, fileListId, previewId, deleteFlag) {

  let dropArea =  document.getElementById(dropAreaId);

  //브라우저에서 드랍 관련한 기본 이벤트가 존재, 초기화하고 진행
  function preventDefaults(e) {
    e.preventDefault();
    e.stopPropagation();
  }

  //드랍존에 접근했을 때 
  function highlight(e) {
    preventDefaults(e);
    dropArea.classList.add("highlight");
  }

  //드랍존에서 벗어남
  function unhighlight(e) {
    preventDefaults(e);
    dropArea.classList.remove("highlight");
  }

  //드랍존에 파일이 들어옴
  function handleDrop(e) {
    unhighlight(e);
    let dt = e.dataTransfer;
    let files = dt.files;
    console.log(files)

    const fileList = document.getElementById(fileListId);
    if (fileList) {
      fileList.scrollTo({ top: fileList.scrollHeight });
    }

  //드래그된 파일로 대체해주기
  if(!fileValidation(files, files[0].name)){
    return false;
  }
    var delete_target = document.getElementById(deleteFlag).value
    delete_target = 'False';
    
    var $file = document.getElementById(fileListId);
    $file.files = files;
    renderFile(files);
  }

  //각각의 파일 미리보기 렌더링
  function renderFile(files){
    var frame = document.getElementById(previewId);
    const reader = new FileReader();
    deleteChilds(frame);
    
    reader.addEventListener('load', () => {
    const img = document.createElement('IMG');
    img.classList.add('thumbnail');
    img.src = reader.result;
    img.setAttribute("width", "150px");
    
    frame.insertAdjacentElement('beforeend', img);
  });
    reader.readAsDataURL(files[0]);
  }

  dropArea.addEventListener("dragenter", highlight, false);
  dropArea.addEventListener("dragover", highlight, false);
  dropArea.addEventListener("dragleave", unhighlight, false);
  dropArea.addEventListener("drop", handleDrop, false);

}
const dropAreaList = ['drop-file-morning','drop-file-lunch','drop-file-dinner','drop-file-snack'];
const fileList = ['morning_diet','lunch_diet','dinner_diet','snack_diet'];
const previewList = ['morining-pre','lunch-pre','dinner-pre','snack-pre'];
const deleteFlag = ['morning_delete_flag','lunch_delete_flag','dinner_delete_flag','snack_delete_flag'];

for (let i=0; i<dropAreaList.length; i++){
    var dropFile = new DropFile(dropAreaList[i], fileList[i], previewList[i], deleteFlag[i]);
}

function inputRenderFile(id, files){
  if(!fileValidation(files, files[0].name)){
    return false;
  }

  var target = null;
  const reader = new FileReader();

  if (id == 'morning_diet'){
    target = document.getElementById(previewList[0]);
    document.getElementById(deleteFlag[0]).value = 'False'

  }else if(id == 'lunch_diet'){
    target = document.getElementById(previewList[1]);
    document.getElementById(deleteFlag[1]).value = 'False'

  }else if(id == 'dinner_diet'){
    target = document.getElementById(previewList[2]);
    document.getElementById(deleteFlag[2]).value = 'False'

  }else{
    target = document.getElementById(previewList[3]);
    document.getElementById(deleteFlag[3]).value = 'False'
  }

  deleteChilds(target);
  reader.addEventListener('load', () => {
  const img = document.createElement('IMG');
  img.classList.add('thumbnail');
  img.src = reader.result;
  img.setAttribute("width", "150px");
  
  target.insertAdjacentElement('beforeend', img);
  });
    reader.readAsDataURL(files[0]);
}

function deleteImage(id){
  var target = null;
  var $file = null;

  if (id == 'delete_morning_diet'){
    document.getElementById(deleteFlag[0]).value = 'True';
    target = document.getElementById(previewList[0]);
    $file = document.getElementById(fileList[0]);

  }else if(id == 'delete_lunch_diet'){
    document.getElementById(deleteFlag[1]).value = 'True';
    target = document.getElementById(previewList[1]);
    $file = document.getElementById(fileList[1]);

  }else if(id == 'delete_dinner_diet'){
    document.getElementById(deleteFlag[2]).value = 'True';
    target = document.getElementById(previewList[2]);
    $file = document.getElementById(fileList[2]);

  }else{ // snack
    document.getElementById(deleteFlag[3]).value = 'True';
    target = document.getElementById(previewList[3]);
    $file = document.getElementById(fileList[3]);
  }
  deleteChilds(target);
  $file.files = null;
  $file.select();
  document.selection.clear();
}

function validationCheck(){
  const form = document.getElementById('daily_form');

  if(document.getElementById(fileList[0]).value){
    form.submit();
  }
  else if(document.getElementById(fileList[1]).value){
    form.submit();
  }
  else if(document.getElementById(fileList[2]).value){
    form.submit();
  }
  else if(document.getElementById(fileList[3]).value){
    form.submit();
  }
  else {
    alert("파일을 1개 이상 첨부해주세요.");
    return false;
  }
}

function fileValidation(file, fileName){
  /* 파일 크기 검사 */
  var fileSize = file.size;
  var maxSize = 3 * 1024 * 1024; //3mb  // 1024*1024 = 1048579 = 1mb
  
  // 1) 파일용량 체크
  if(fileSize > maxSize){ // 용량 초과시
    var msg = maxSize / 1048576 + "MB 이하의 파일만 업로드 가능합니다.";
    alert(msg);
    return false;
  }
    
  if (fileName != "") {
    var ext = fileName.slice(fileName.lastIndexOf(".") + 1).toLowerCase();
    if (!(ext == "gif" || ext == "jpg" || ext == "png")) {
        alert("이미지파일 (.jpg, .png, .gif ) 만 업로드 가능합니다.");
        return false;
    }
}
  return true;
}