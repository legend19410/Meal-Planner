function generateMealPlan(event){
    axios.post('/user/meal_plan', {'date':event.currentTarget.id},{
        headers: {
            'Content-Type':'application/json'
        }
    })
    .then(()=>{
        location.reload()
    })
}

function regenerateMealPlan(event){
    axios.patch('/user/meal_plan', {'date':event.currentTarget.id.substring(0,10)},{
        headers: {
            'Content-Type':'application/json'
        }
    })
    .then(()=>{
        location.reload()
    })
}

function deleteMealPlan(event){
    axios.delete('/user/meal_plan', {
        data:{'date':event.currentTarget.id.substring(0, 10)},
        headers: {
            'Content-Type':'application/json'
        }    
    })
    .then(()=>{
        location.reload()
    })
}