window.onload = (event) => {
    const atobuttons = document.querySelectorAll(".add-to-btn");
    const addbuttons = document.querySelectorAll(".addbtn");
    const cancelbuttons = document.querySelectorAll(".btn-cancel");
    for (let i=0; i <atobuttons.length;i++){
        atobuttons[i].onclick = function () {
            document.getElementById("popupForm-"+(i+1)).style.display = "block";
        }
        console.log(atobuttons[i]);
        // console.log(buttons[i]);
        
    }

    for (let i=0; i <cancelbuttons.length;i++){
        cancelbuttons[i].onclick = function () {
            document.getElementById("popupForm-"+(i+1)).style.display = "none";
        }
        console.log(cancelbuttons[i]);
        // console.log(buttons[i]);
        
    }
    
    for (let i=0; i <addbuttons.length;i++){
        addbuttons[i].onclick = function () {
            let unit = document.getElementById("units-"+(i+1)).value;
            console.log("units-"+(i+1));
            let quantity = document.getElementById("quantity-"+(i+1)).value;
            console.log(fetch('http://localhost:5000/user/add_to_kitchen/'+addbuttons[i].id+"/"+unit+"/"+quantity));
            fetch('/user/add_to_kitchen/'+addbuttons[i].id+"/"+unit+"/"+quantity)
            .then(response => response.json())
            .then(data => console.log(data));

            // document.getElementById("popupForm-"+addbuttons[i].id).style.display = "block";
        }
        // console.log(buttons[i].id);
        // console.log(buttons[i]);
        
    }

  };

function openForm() {
    document.getElementById("popupForm").style.display = "block";
}

function closeForm() {
document.getElementById("popupForm").style.display = "none";
}    