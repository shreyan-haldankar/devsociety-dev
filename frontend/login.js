let form = document.getElementById('login-form')

//  Whenever the form gets submit, our event listener will:
form.addEventListener('submit', (e) => {
    e.preventDefault()
    // Prevent the default function of the refreshing the form

    let formData = {
        'username': form.username.value,
        'password': form.password.value
    }

    fetch('http://127.0.0.1:8000/api/users/token/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData)
    })

    .then(response => response.json())
    .then(data => {
        console.log("DATA: ", data.access)
        if(data.access){
            localStorage.setItem('token', data.access)
            window.location = "http://127.0.0.1:5500/projects-list.html"
        }
        else{
            alert("Username or password did not work!")
        }
    })
})