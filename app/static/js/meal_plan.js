function generateMealPlan(event){
    axios.post('/user/meal_plan', {'date':event.target.id},{
        headers: {
            'Content-Type':'application/json'
        }
    })
    .then(()=>{
        location.reload()
    })
}

function deleteMealPlan(event){
    console.log(event.currentTarget.id.substring(0, 10))
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