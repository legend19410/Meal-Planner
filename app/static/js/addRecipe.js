var addIngredientBtn = document.getElementById('add-ingredient');
var addInstructionBtn = document.getElementById('add-instruction');
var addRecipeBtn = document.getElementById('add-recipe-btn');

function createIngredientInput(){
    var containerDiv = document.createElement('div');
    containerDiv.classList.add(...["ingredient", "mb-3"]);

    var quantityInput = document.createElement('input');
    quantityInput.classList.add(...['form-control', 'quantity']);
    quantityInput.setAttribute('type', 'number');
    quantityInput.setAttribute('placeholder', 'Amount');

    containerDiv.appendChild(quantityInput);

    var selectUnits = document.createElement('select');
    selectUnits.classList.add(...['form-select', 'units']);
    selectUnits.setAttribute('name','units');
    var option0 = document.createElement("option");
    var option1 = document.createElement("option");
    var option2 = document.createElement("option");
    option0.text = "lb";
    option0.value = "lb";
    selectUnits.add(option0)
    option1.text = "cup";
    option1.value = "cup";
    selectUnits.add(option1)
    option2.text = "g";
    option2.value = "g";
    selectUnits.add(option2);

    containerDiv.appendChild(selectUnits);

    var ingredientName = document.createElement('select');
    ingredientName.classList.add(...['form-select']);
    ingredientName.setAttribute('name','ingredient');
    var option0 = document.createElement("option");
    var option1 = document.createElement("option");
    var option2 = document.createElement("option");
    option0.text = "Rice";
    option0.value = "1";
    ingredientName.add(option0)
    option1.text = "Pop Choi";
    option1.value = "2";
    ingredientName.add(option1)
    option2.text = "Chicken";
    option2.value = "3";
    ingredientName.add(option2);

    containerDiv.appendChild(ingredientName);

    var deleteBtn = document.createElement('button');
    deleteBtn.setAttribute('type', 'button');
    deleteBtn.classList.add(...['btn', 'btn-outline-primary','btn-sm','delete'])
    var deleteIcon = document.createElement('i');
    deleteIcon.classList.add(...['fas','fa-trash']);
    deleteBtn.appendChild(deleteIcon);
    deleteBtn.addEventListener('click', deleteIngredientDiv)

    containerDiv.appendChild(deleteBtn);

    return containerDiv;
}

function deleteIngredientDiv(event){
    event.currentTarget.parentElement.remove();
}


function createInstructionInput(){
    var containerDiv = document.createElement('div');
    containerDiv.classList.add(...["instruction", "mb-3"]);

    var stepInput = document.createElement('input');
    stepInput.classList.add(...['form-control', 'step']);
    stepInput.setAttribute('type', 'number');
    stepInput.setAttribute('placeholder', 'Step');

    containerDiv.appendChild(stepInput);

    var instructionDescription = document.createElement('input');
    instructionDescription.setAttribute('type','text');
    instructionDescription.setAttribute('name', 'instruction');
    instructionDescription.setAttribute('placeholder', "Enter instruction");
    instructionDescription.classList.add(...['form-control']);

    containerDiv.appendChild(instructionDescription);

    var deleteBtn = document.createElement('button');
    deleteBtn.setAttribute('type', 'button');
    deleteBtn.classList.add(...['btn', 'btn-outline-primary','btn-sm','delete'])
    var deleteIcon = document.createElement('i');
    deleteIcon.classList.add(...['fas','fa-trash']);
    deleteBtn.appendChild(deleteIcon);
    deleteBtn.addEventListener('click', deleteInstructionDiv)

    containerDiv.appendChild(deleteBtn);

    return containerDiv;
}

function deleteInstructionDiv(event){
    event.currentTarget.parentElement.remove();
}

addIngredientBtn.onclick = ev =>{
    document.getElementById('ingredients').appendChild(createIngredientInput())
};

addInstructionBtn.onclick = ev =>{
    document.getElementById('instructions').appendChild(createInstructionInput())
};


addRecipeBtn.onclick = ev =>{
    ev.preventDefault();

    var recipeName = document.getElementById('recipe-name').value;
    var image = document.getElementById('image').files[0]; 

    var ingredients = []
    var ingredientsDivs =  document.getElementsByClassName('ingredient');
    
    for(let div of ingredientsDivs){
        let ingredient = {
            "quantity": Number.parseInt(div.children[0].value),
            "units": div.children[1].value,
            "ingredient_id": Number.parseInt(div.children[2].value)
        }
        if(div.children[2].value!=null && div.children[2].value!=null){
            ingredients.push(ingredient);
        }
    }

    var instructions = []
    var instructionsDivs =  document.getElementsByClassName('instruction');

    for(let div of instructionsDivs){
        let instruction = {
            "step_no": Number.parseInt(div.children[0].value),
            "description": div.children[1].value,
        }
        if(div.children[1].value!=null && div.children[1].value!=null){
            instructions.push(instruction);
        }
    }

    var recipeForm = new FormData();

    recipeForm.append('name',recipeName);
    recipeForm.append('image', image, image.name);

    recipeForm.append('ingredients', JSON.stringify(ingredients));
    recipeForm.append('instructions', JSON.stringify(instructions));

    axios.post('/user/add-recipe', recipeForm, {
        headers: {
            'Content-Type':'multipart/form-data'
        }
    })
    .then((resp)=>{
        console.log(resp.status+', '+resp.statusText);
    })
    .catch((err)=>{
        console.log(err)
    });
};