
const showUpdateBtns = document.querySelectorAll(".show-update")
showUpdateBtns.forEach(btn => {
    btn.addEventListener("click", showUpdateForm)
})

const updateBtns = document.querySelectorAll(".update-post");
updateBtns.forEach(btn => {
    btn.addEventListener("click", updatePost)
})

function showUpdateForm() {
    const postId = Number(this.dataset.postid);
    const form = document.querySelector(`.profile-post-${postId} div.update-post-form`)
    this.style.display = "none";
    form.style.display = "block";
}

function updatePost() {
    const postId = Number(this.dataset.postid);
    const post = document.querySelector(`.profile-post-${postId}`)
    const form = post.querySelector("div.update-post-form");
    const title = form.querySelector("input[name='title']").value; 
    const text = form.querySelector("textarea").value; 

    fetch("http://localhost:8000/reddit/posts/" + postId, {
        method: "PATCH",
        credentials: "include",
        headers: {
            Accept: "application/json",
                    "Content-Type": "application/json",
                    "X-CSRFToken": getCookie("csrftoken")
        },
        body: JSON.stringify({ title, text })
      })
    .then(res => {
        if (res.ok) {
            const specificForm = document.querySelector(`.profile-post-${postId} div.update-post-form`);
            const specificBtn = document.querySelector(`.btn-${postId}`)
            const newTitle = post.querySelector("h3");
            const newText = post.querySelector("p");
            newTitle.textContent = title
            newText.textContent = text
            specificForm.style.display = "none";
            specificBtn.textContent = "Updated";
            specificBtn.style.display = "block";
        }
    })
    
}