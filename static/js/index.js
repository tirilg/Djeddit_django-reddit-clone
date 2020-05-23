
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        var cookies = document.cookie.split(";");
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === name + "=") {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


const voteArrows = document.querySelectorAll(".post-vote");

voteArrows.forEach(arrow => {
    arrow.addEventListener("click", handleVote)
})



function handleVote() {
    const postId = Number(this.dataset.postid);
    const userId = Number(this.dataset.userid);
    const votes = Number(this.dataset.votes);

    let vote = null;

    if (this.classList.contains("upvote")) {
        vote = true;
    } else {
        vote = false;
    }
    sendVote(postId, userId, vote)
    updateVotes(postId, vote, votes)
}

function getVotes() {
    fetch("http://127.0.0.1:8000/reddit/votes", {
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
          "X-CSRFToken": getCookie("csrftoken")
        },
        credentials: "include",
      })
    .then(res => res.json())
    .then(data => {
            console.log(data)
    })
}

function updateVotes(postId, vote, votes) {
    fetch("http://127.0.0.1:8000/reddit/posts/" + postId, {
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
          "X-CSRFToken": getCookie("csrftoken")
        },
        credentials: "include",
        method: "PATCH",
        body: JSON.stringify({ votes: vote ? votes + 1 : votes - 1 })
      })
    .then(res => res.json())
    .then(data => {
        const voteCount = document.querySelector(`.post-${postId} .votes`)
        const currentVotes = Number(voteCount.textContent)
        voteCount.textContent = vote ? currentVotes + 1 : currentVotes - 1;
    })
}

function sendVote(postId, userId, vote) { 
    fetch("http://127.0.0.1:8000/reddit/votes/", {
        headers: {
            Accept: "application/json",
            "Content-Type": "application/json",
            "X-CSRFToken": getCookie("csrftoken")
        },
        method: "POST",
        credentials: "include",
        body: JSON.stringify({ post: postId, user: userId, vote: vote })
      })
    .then(res => res.json())
    .then(data => {
        console.log(data)
    })
    .catch(err => {
        console.log(err)
    })
}

function fetchPosts() {
    fetch("http://127.0.0.1:8000/reddit/posts", {
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
          "X-CSRFToken": getCookie("csrftoken")
        },
        credentials: "include",
      })
        .then(res => res.json())
        .then(data => {
            console.log(data)
        })
}

fetchPosts()
getVotes()