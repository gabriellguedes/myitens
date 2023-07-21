const inputFile = document.querySelector("#id_gallery-0-original");
const pictureImage = document.querySelector(".picture__image");
const pictureImageTxt = "Choose an image";
pictureImage.innerHTML = pictureImageTxt;

inputFile.addEventListener("change", function (e) {
  var preview = document.getElementById("preview");

  const inputTarget = e.target;
  const file = inputTarget.files[0];

  if (file) {
    preview.classList.remove("hidee");

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
    pictureImage.innerHTML = pictureImageTxt;
  }
});
