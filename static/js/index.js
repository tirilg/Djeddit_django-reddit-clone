
// Vote buttons
const voteArrows = document.querySelectorAll(".post-vote");
voteArrows.forEach(arrow => {
    arrow.addEventListener("click", handleVote)
})

// Create post button
const createBtn = document.querySelector("#create-post");
createBtn.addEventListener("click", createPost);


function handleVote() {
    const postId = Number(this.dataset.postid);
    const userId = Number(this.dataset.userid);
    const votes = Number(this.dataset.votes);

    let vote = null;
    let clicked = null;

    if (this.classList.contains("upvote")) {
        vote = true;
        if (this.classList.contains("clicked")) {
            this.classList.remove("clicked")
            clicked = false;
        } else {
            this.classList.add("clicked")
            clicked = true;
        }
    } else {
        vote = false;
        if (this.classList.contains("clicked")) {
            this.classList.remove("clicked")
            clicked = false;
        } else {
            this.classList.add("clicked")
            clicked = true;
        }

    }
    sendVote(postId, userId, vote)
    updateVotes(postId, vote, votes, clicked)
}

function getVotes() {
    fetch("http://127.0.0.1:8000/reddit/votes", {
        credentials: "include",
        headers: {
            Accept: "application/json",
                    "Content-Type": "application/json",
                    "X-CSRFToken": getCookie("csrftoken")
        },
      })
    .then(res => res.json())
    .then(data => {
        console.log(data)
    })
}


function updateVotes(postId, vote, votes, clicked) {
    fetch("http://127.0.0.1:8000/reddit/posts/" + postId, {
        method: "PATCH",
        credentials: "include",
        headers: {
            Accept: "application/json",
                    "Content-Type": "application/json",
                    "X-CSRFToken": getCookie("csrftoken")
        },
        body: JSON.stringify({ votes: vote ? votes + 1 : votes - 1 })
      })
    .then(res => {
        console.log(res)
        if(res.ok) {
            const voteCount = document.querySelector(`.post-${postId} .votes`)
            const currentVotes = Number(voteCount.textContent)
            if(clicked) {
                voteCount.textContent = vote ? currentVotes + 1 : currentVotes - 1;
            }
        }
    })
}

function sendVote(postId, userId, vote) { 
    fetch("http://127.0.0.1:8000/reddit/votes/", {
        method: "POST",
        redirect: 'follow',
        credentials: "include",
        headers: {
            Accept: "application/json",
                    "Content-Type": "application/json",
                    "X-CSRFToken": getCookie("csrftoken")
        },
        body: JSON.stringify({ post: postId, user: userId, vote: vote })
      })
    .then(res => {
        if (res.redirected) {
            window.location.href = res.url;
        }
    })
    .then(data => {
        console.log(data)
    })
    .catch(err => {
        console.log(err)
    })
}

function fetchPosts() {
    fetch("http://127.0.0.1:8000/reddit/posts", {
        credentials: "include",
        headers: {
            Accept: "application/json",
                    "Content-Type": "application/json",
                    "X-CSRFToken": getCookie("csrftoken")
        }
      })
    .then(res => res.json())
    .then(data => {
        console.log(data)
     })
}


function createPost(e) {
    e.preventDefault();
    const form = document.querySelector(".post-form");
    const title = form.querySelector("input[name='title']").value; 
    const text = form.querySelector("textarea").value;
    const author = form.querySelector("input[name='user_id']").value;

    const postList = document.querySelector("#posts")

    fetch("http://127.0.0.1:8000/reddit/posts/", {
        method: "POST",
        credentials: "include",
        headers: {
            Accept: "application/json",
                    "Content-Type": "application/json",
                    "X-CSRFToken": getCookie("csrftoken")
        },
        body: JSON.stringify({ title, text, author })
    })
    .then(res => {
        console.log(res)
        if(!res.ok) {
            console.log("something went wrong")
            return false;
        } else {
            return res.json();
        }
    })
    .then(data => {
        console.log(data)
        if (data !== false) {
            const bluePrint = `<div class="post-container post-${data.id}" style="border: 1px solid black; margin-bottom: 10px;">
            <div>             
                <p class="upvote post-vote" data-votes="${data.votes}" data-postid="${data.id}" data-userid="${data.author}">&uarr;</p>
                <p class="votes">${data.votes}</p>
                <p class="downvote post-vote" data-votes="${data.votes}" data-postid="${data.id}" data-userid="${data.author}">&darr;</p>
            </div>
            <div class="post">
                <a href={% url 'reddit_app:single_post' post.id %}>
                    <h3>${data.title}</h3>
                    <div class="post-info">
                        <span>Posted by: ${data.author}</span>
                        <p>${data.created_at}</p>
                    </div>
                    <p>${data.text}</p>
                </a>
            </div>
        </div>`
    
            postList.insertAdjacentHTML("afterbegin", bluePrint);
        }

    })
    .catch(err => {
        console.log(err)
    })
}

fetchPosts()
getVotes()