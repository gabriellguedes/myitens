const inputFile = document.querySelector("#id_gallery-0-original");
const pictureImage = document.querySelector(".picture__image");
const pictureImageTxt = "Choose an image";
pictureImage.innerHTML = pictureImageTxt;

inputFile.addEventListener("change", function (e) {
  const preview = document.getElementById("preview");
  const boxPhotos = document.getElementById("boxPhotos");
  const buttoms = document.getElementById("boxButtonsPreview");
  const msg = document.getElementById("box_msg");

  const inputTarget = e.target;
  const file = inputTarget.files[0];

  if (file) {
    preview.classList.remove("hidee");
    
    boxPhotos.classList.remove("d-block");
    boxPhotos.classList.add("d-none");
    
    buttoms.classList.remove("d-none");
    buttoms.classList.add("d-block");

    msg.classList.remove("d-none");
    msg.classList.add("d-block");

    const reader = new FileReader();

    reader.addEventListener("load", function (e) {
      const readerTarget = e.target;

      const img = document.createElement("img");
      img.src = readerTarget.result;
      img.classList.add("picture__img");

      pictureImage.innerHTML = "";
      pictureImage.appendChild(img);
    });

    reader.readAsDataURL(file);
  } else {
    preview.classList.add("hidee");
    
    boxPhotos.classList.remove("d-none");
    boxPhotos.classList.add("d-block");
    
    buttoms.classList.remove("d-block");
    buttoms.classList.add("d-none");

    msg.classList.remove("d-block");
    msg.classList.add("d-none");

    pictureImage.innerHTML = pictureImageTxt;
  }
});
