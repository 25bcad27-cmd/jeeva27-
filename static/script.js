document.getElementById("form").addEventListener("submit", function(e) {
    let phone = document.querySelector("input[name='phone']").value;

    if (phone.length !== 10 || isNaN(phone)) {
        alert("Enter a valid 10-digit phone number");
        e.preventDefault();
    }
});