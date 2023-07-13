window.onload = function() {  
    var button_pwd = document.getElementById("showpassword");

    button_pwd.addEventListener("click", function(){
        var tipo = document.getElementById("id_password");
        var icon = document.getElementById("icon_show_password");

        if(tipo.type === "password"){
            tipo.type = "text";
            icon.classList.remove("fa-eye");
            icon.classList.add("fa-eye-slash");
        }else{
            tipo.type = "password";
            icon.classList.remove("fa-eye-slash");
            icon.classList.add("fa-eye");
        }
    });
};    
const postContainer = document.getElementById('posts-container')
const loading = document.querySelector('.loader');
const filter = document.getElementById('filter');

let limit = 5;
let page = 1;

async function getPosts () {
  const res = await fetch(
    `https://jsonplaceholder.typicode.com/posts?_limit=${limit}&_page=${page}`
  );

  const data = await res.json();

  return data;
}

async function showPosts() {
  const posts = await getPosts()
  posts.forEach(post => {
    const postEl = document.createElement('div');
    postEl.classList.add('post');
    postEl.innerHTML = `
      <div class="post-info">
        <h2 class="post-title">${post.title}</h2>
        <p class="post-body">${post.body}</p>
      </div>
    `;

    postContainer.appendChild(postEl)
  });
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
showPosts()


function showLoading() {
  loading.classList.add('show');

  setTimeout(() => {
    loading.classList.remove('show')

    setTimeout(() => {
      page++;
      showPosts();
    }, 300);
  }, 1000)
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


