
var redimensionar  = $('#preview_photo').croppie({
	enableExif: true,
	enableOrientation: true,
	viewport: {
		width: 300,
		height: 300,
		type: 'circle'
	},
	boundary: {
		width: 400,
		height:400,
	}
});
const pictureImageTxt = "Choose an image";

redimensionar.innerHTML = pictureImageTxt;

$('#id_gallery-0-original').on('change', function(){
	var reader = new FileReader();
	const preview = document.getElementById("preview");
  	const boxPhotos = document.getElementById("boxPhotos");
  	const buttoms = document.getElementById("boxButtonsPreview");
  	const msg = document.getElementById("box_msg");

	if (reader){
		preview.classList.remove("hidee");
    
	    boxPhotos.classList.remove("d-block");
	    boxPhotos.classList.add("d-none");
	    
	    buttoms.classList.remove("d-none");
	    buttoms.classList.add("d-block");

	    msg.classList.remove("d-none");
	    msg.classList.add("d-block");

		reader.onload = function(e){
			redimensionar.croppie('bind', {
				url: e.target.result
			}); 
		}
	} else {
		preview.classList.add("hidee");
    
	    boxPhotos.classList.remove("d-none");
	    boxPhotos.classList.add("d-block");
	    
	    buttoms.classList.remove("d-block");
	    buttoms.classList.add("d-none");

	    msg.classList.remove("d-block");
	    msg.classList.add("d-none");

	    redimensionar.innerHTML = pictureImageTxt;
	}

	reader.readAsDataURL(this.files[0]);

	
});


$('#btn-upload-imagem').on('click', function(){
	redimensionar.croppie('result', {

		type:'canvas',
		size: 'viewport',
	}).then(function (img) {
		$.ajax({
			url: "",
			type: "POST",
			data:{
				"imagem": img
			},
			success: function(){
				alert("Imagem enviada com sucesso!")
			}
		});
	});
});
