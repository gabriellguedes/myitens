window.onload = function() {  
    var button_pwd = document.getElementById("showpassword");

    button_pwd.addEventListener("click", function(){
        var tipo = document.getElementById("id_password");
        var icon = document.getElementById("icon_show_password");

        if(tipo.type === "password"){
            tipo.type = "text";
            icon.classList.remove("fa-eye");
            icon.classList.add("fa-eye-slash");
            icon.removeAttribute('title');
            icon.setAttribute('title', 'Esconder Senha');
        }else{
            tipo.type = "password";
            icon.classList.remove("fa-eye-slash");
            icon.classList.add("fa-eye");
            icon.removeAttribute('title');
            icon.setAttribute('title', 'Mostrar Senha');
        }
    });

    var checkbox = document.getElementById("check_termos");

    checkbox.addEventListener("change", function(){
        var btn = document.getElementById("btn_new_user");

        if (checkbox.checked == true) {
            btn.removeAttribute('disabled');
        }else{
            btn.setAttribute('disabled', '');
        }
    });

};    
const postContainer = document.getElementById('posts-container')
const loading = document.querySelector('.loader');
const filter = document.getElementById('filter');

let limit = 10;
let page = 1;

async function getPosts() {
/* `https://jsonplaceholder.typicode.com/posts?_limit=${limit}&_page=${page}`*/
const res =  fetch(
    `http://192.168.102.13:8000/api/?page=${page}`
  ).then((response) => {
    response.json().then((dados) => {
        dados.results.map((result) => {
            postContainer.innerHTML += `
                <div class="post">
                  <div class="post-info">
                    <h2 class="post-title">${result.id}</h2>
                    <p class="post-body">
                        <ul class="row">
                            <li class="col text-center">${result.num1}</li>
                            <li class="col text-center">${result.num2}</li>
                            <li class="col text-center">${result.num3}</li>
                            <li class="col text-center">${result.num4}</li>
                            <li class="col text-center">${result.num5}</li>
                            <li class="col text-center">${result.num6}</li>
                        </ul>
                    </p>
                    <small class="text-danger">${result.date}</small>
                  </div>
                </div>
            `;
        })
    })
  })

}


function filterPosts(e) {
  const term = e.target.value.toUpperCase();
  const posts = document.querySelectorAll('.post');

  posts.forEach(post => {
    const title = post.querySelector('.post-title').innerText.toUpperCase();
    const body = post.querySelector('.post-body').innerText.toUpperCase();

    if (title.indexOf(term) > -1 || body.indexOf(term) > -1) {
      post.style.display = 'flex';
    } else {
      post.style.display = 'none';
    }
  });
}
getPosts()


function showLoading() {
  loading.classList.add('show');

  setTimeout(() => {
    loading.classList.remove('show')

    setTimeout(() => {
      page++;
      getPosts();
    }, 30);
  }, 100)
}

window.addEventListener('scroll', () => {
  const { scrollTop, scrollHeight, clientHeight } = document.documentElement;

  if (scrollTop + clientHeight >= scrollHeight -5) {
    showLoading()
  }
});



filter.addEventListener('input', filterPosts)


 var button = document.getElementById("responsive_button_search");

    button.addEventListener("click", function() {
      var field = document.getElementById("container_search_field");

      field.classList.toggle("hide");
    });


function editBio(){
    const modal = document.getElementById('modal-container-bio')
    modal.classList.add('mostrar')

    modal.addEventListener('click', (e) =>{
        if (e.target.id == "fechar" || e.target.id=="btn-fechar"){
            modal.classList.remove('mostrar')
            localStorage.fechaModal = 'modal-container'
        }
    })
}

function editProfile(){
    const modal = document.getElementById('modal-container-editprofile')
    modal.classList.add('mostrar')

    modal.addEventListener('click', (e) =>{
        if (e.target.id == 'modal-container' || e.target.id == "fechar" || e.target.id=="btn-fechar"){
            modal.classList.remove('mostrar')
            localStorage.fechaModal = 'modal-container'
        }
    })
}

function editCapa(){
    const modal = document.getElementById('modal-container-capa')
    modal.classList.add('mostrar')

    modal.addEventListener('click', (e) =>{
        if (e.target.id == 'modal-container' || e.target.id == "fechar" || e.target.id=="btn-fechar"){
            modal.classList.remove('mostrar')
            localStorage.fechaModal = 'modal-container'
        }
    })
}

function editPhoto(){
    const modal = document.getElementById('modal-container-photo')
    modal.classList.add('mostrar')

    modal.addEventListener('click', (e) =>{
        if (e.target.id == "fechar" || e.target.id=="btn-fechar"){

            var inputFile = document.getElementById('id_gallery-0-original');
            var formulario = document.getElementById('form_update_photo');
            inputFile.value='';
            formulario.reset();

            modal.classList.remove('mostrar')
            localStorage.fechaModal = 'modal-container'
        }
    })
}
