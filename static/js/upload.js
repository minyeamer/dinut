function DropFile(dropAreaId, fileListId) {
  let dropArea = document.getElementById(dropAreaId);
  let fileList = document.getElementById(fileListId);

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

    handleFiles(files);

    const fileList = document.getElementById(fileListId).val;
    if (fileList) {
      fileList.scrollTo({ top: fileList.scrollHeight });
    }
  }
  
  //html에 표시 해줄 파일 배열 추출 
  function handleFiles(files) {
    var $file = document.getElementById("chooseFile");
    
    if(!fileValidation(files, files[0].name)){
      return false;
    }

    let tumbnail = document.querySelector('.thumbnail');
    let details =  document.querySelector('.details');
    let title =  document.getElementById("message_text");
    if (title != null){
      title.remove();
    }

    if ( tumbnail != null || details != null){
      var fileArea = document.querySelector('#fileArea');
      fileArea.parentNode.removeChild(fileArea);
      $file.files = null;
    }

    LoadImg(files);
    
    $file.files = files;
    files = [...files];
    files.forEach(previewFile);
  }
  
  function LoadImg(files) {
    var reader = new FileReader();
    var previewImage = document.getElementById("previewImage");
      reader.addEventListener('load', () => {
      previewImage.setAttribute("width", "300px");
      previewImage.src = reader.result;
      });
      reader.readAsDataURL(files[0]);
  }

  function previewFile(file) {
    fileList.appendChild(renderFile(file));
  }
  
  function renderFile(file) {
    let fileDOM = document.createElement("div");
    fileDOM.className = "file";
    fileDOM.id ='fileArea';
    fileDOM.innerHTML = `
      <div class="thumbnail">
        <img src="https://img.icons8.com/pastel-glyph/2x/image-file.png" alt="파일타입 이미지" class="image">
      </div>
      <div class="details">
        <header class="header">
          <span class="name">${file.name}</span>
          <span class="size">${file.size}</span>
        </header>
        <div class="progress">
          <div class="bar"></div>
        </div>
        <div class="status">
          <span class="percent">100% done</span>
          <span class="speed">90KB/sec</span>
        </div>
      </div>
    `;
    return fileDOM;
  }

  dropArea.addEventListener("dragenter", highlight, false);
  dropArea.addEventListener("dragover", highlight, false);
  dropArea.addEventListener("dragleave", unhighlight, false);
  dropArea.addEventListener("drop", handleDrop, false);

  return {
    handleFiles
  };
}

const dropFile = new DropFile("drop-file", "files");

function fileValidation(file, fileValue){
  /* 파일 크기 검사 */
  var fileSize = file.size;
  var maxSize = 3 * 1024 * 1024; //3mb  // 1024*1024 = 1048579 = 1mb
  
  // 1) 파일용량 체크
  if(fileSize > maxSize){ // 용량 초과시
    var msg = maxSize / 1048576 + "MB 이하의 파일만 업로드 가능합니다.";
    alert(msg);
    return false;
  }
    
  if (fileValue != "") {
    var ext = fileValue.slice(fileValue.lastIndexOf(".") + 1).toLowerCase();
    if (!(ext == "gif" || ext == "jpg" || ext == "png")) {
        alert("이미지파일 (.jpg, .png, .gif ) 만 업로드 가능합니다.");
        return false;
    }
}
  return true;
}