// Update post buttons
const updateBtns = document.querySelectorAll(".update-post");
updateBtns.forEach(btn => {
    btn.addEventListener("click", updatePost)
})

function updatePost() {
    const postId = Number(this.dataset.postid);
    const form = document.querySelector(".update-post-form");
    const title = form.querySelector("input[name='title']").value; 
    const text = form.querySelector("textarea").value; 

    fetch("http://127.0.0.1:8000/reddit/posts/" + postId, {
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
            this.textContent = 'Updated';
        }
        console.log(res)
        console.log(this)
    })
    
}