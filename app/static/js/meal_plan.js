function generateMealPlan(event){
    axios.post('/user/meal_plan', {'date':event.target.id},{
        headers: {
            'Content-Type':'application/json'
        }
    })
}