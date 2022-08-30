// Get search form and page links
let searchForm = document.getElementById("searchForm");
let pageLinks = document.getElementsByClassName("page-link");

// Ensure search form exists
if (searchForm) {
  for (let i = 0; i < pageLinks.length; i++) {
    pageLinks[i].addEventListener("click", function (e) {
      e.preventDefault();
      // GET DATA ATTRIBUTES

      // this is the current button that we clicked on
      let page = this.dataset.page;

      // ADD HIDDEN SEARCH INPUT TO FORM
      searchForm.innerHTML += `<input value=${page} name="page" hidden/>`;

      // SUBMIT FORM
      searchForm.submit();
    });
  }
}


// For removing tags from projects

let tags = document.getElementsByClassName('project-tag')

for(let i = 0; i < tags.length; i++)
{
  tags[i].addEventListener('click', (e) => {
    let tagId = e.target.dataset.tag
    let projectId = e.target.dataset.project

    // console.log('Tag Id: ', tagId)
    // console.log('Project Id: ', projectId)

    fetch('http://127.0.0.1:8000/api/remove-tag/', {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({'project': projectId, 'tag': tagId})
    })
    .then(response => response.json())
    .then(data => {
      e.target.remove()
    
    }
    )

  })
}