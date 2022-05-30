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

    const fileList = document.getElementById(fileListId);
    if (fileList) {
      fileList.scrollTo({ top: fileList.scrollHeight });
    }

  //드래그된 파일로 대체해주기 
    var $file = document.getElementById("chooseFile")
    $file.files = files

  }

  //html에 표시 해줄 파일 배열 추출 
  function handleFiles(files) {
    files = [...files];
    files.forEach(previewFile);
  }

  function previewFile(file) {
    console.log(file);
    fileList.appendChild(renderFile(file));
  }

  function renderFile(file) {
    let fileDOM = document.createElement("div");
    fileDOM.className = "file";
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
