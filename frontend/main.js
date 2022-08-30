let loginBtn = document.getElementById('login-btn')
let logoutBtn = document.getElementById('logout-btn')

let token = localStorage.getItem('token')

if(token){
  loginBtn.remove()
}
else{
  logoutBtn.remove()
}

logoutBtn.addEventListener('click', (e) => {
  e.preventDefault()

  localStorage.removeItem('token')
  window.location = 'http://127.0.0.1:5500/login.html'
})

let projectUrl = "http://127.0.0.1:8000/api/projects/";

// Fetching the api
let getProjects = () => {
  fetch(projectUrl)
    // For converting our response to JSON data
    .then((response) => response.json())
    // After that we are gonna get the json data (the array of objects in json format)
    .then((data) => {
      console.log(data);
      buildProjects(data);
    });
};

let buildProjects = (projects) => {
  let projectsWrapper = document.getElementById("projects--wrapper");
  projectsWrapper.innerHTML = ''

  for (let i = 0; i < projects.length; i++) {
    let project = projects[i];

    let projectCard = `
            <div class="project--card">
                <img src="http://127.0.0.1:8000${project.featured_image}" />
            
                <div>
                    <div class="card--header">
                        <h3>${project.title}</h3>
                        <strong class="vote--option" data-vote="up" data-project="${project.id}">&#43;</strong>
                        <strong class="vote--option" data-vote="down" data-project="${project.id}">&#8722;</strong>

                    </div>
                    <i>${project.vote_ratio}% Positive Feedback</i>
                    <p>${project.description.substring(0, 150)}</p>
                </div>
            </div>
        `;
    projectsWrapper.innerHTML += projectCard;
  }
  // To trigger a POST event
  // Add an Event Listener
  addVoteEvents();
};

// This function is gonna be responsible for adding our vote from the button

let addVoteEvents = () => {
  // Query the vote buttons
  let voteBtns = document.getElementsByClassName("vote--option");

  for (let i = 0; i < voteBtns.length; i++) {
    let token = localStorage.getItem('token')
    console.log("Token: ",token)

    voteBtns[i].addEventListener("click", (e) => {
      let vote = e.target.dataset.vote;
      let project = e.target.dataset.project;

      fetch(`http://127.0.0.1:8000/api/projects/${project}/vote/`, {
        method: 'POST',
        headers: {
          'Content-type':'application/json',
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({'value': vote})
      })

      .then(response => response.json())
      .then(data => {
        console.log("Success: ", data)
        // Anytime a vote is complete loadin more projects, we are adding the same project multiple times
        getProjects();

      })

    });
  }
};

getProjects();
