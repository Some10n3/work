/*
TODO

-hidden on load for dropdown
-visible when logged in

*/


const web = 'http://localhost:8000/'

window.onload = function() {

    document.getElementById('login').addEventListener('click', login);
    document.getElementById('username').addEventListener('keyup', function(event) {
        if (event.keyCode === 13 && document.getElementById('username').value != "") {
            event.preventDefault();
            document.getElementById('login').click();
        }
    });
    document.getElementById('password').addEventListener('keyup', function(event) {
        if (event.keyCode === 13 && document.getElementById('username').value != "") {
            event.preventDefault();
            document.getElementById('login').click();
        }
    });

    document.getElementById('alert').style.display = "none";

}

function login() {
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;

    fetch(web + 'login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            "ID": username,
            "Password": password
        })
    }).then(response => response.json())
    .then(data => {
        if (data.length == 0) {
            document.getElementById('alert').innerHTML = "Wrong username or password!";
            document.getElementById('alert').style.display = "block";
            return;
        }
    });
}