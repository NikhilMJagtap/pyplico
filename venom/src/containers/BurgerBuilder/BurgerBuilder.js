import {Component, Fragment} from 'react';
import Burger from '../../components/Burger/Burger';
import BuildControls from '../../components/Burger/BuildControls/BuildControls'
import OrderSummary from '../../components/Burger/OrderSummary/OrderSummary';

const INGREDIENT_PRICING = {
    salad: 0.5,
    bacon: 1,
    cheese: 0.7,
    meat: 1.2
}

class BurgerBuilder extends Component {

    constructor(props) {
        super(props)
        this.state = {
            ingredients: {
                salad: 0,
                bacon: 0,
                cheese: 0,
                meat: 0
            },
            totalPrice: 4,
            purchasable: false,
            purchasing: false
        }
    }

    addIngredientHandler = (type) => {
        const ingredients = {...this.state.ingredients}
        ingredients[type] += 1;
        const price = this.state.totalPrice + INGREDIENT_PRICING[type];
        this.setState({
            ingredients: ingredients,
            totalPrice: price
        });
        this.updatePurchaseState(ingredients);
    }

    removeIngredientHandler = (type) => {
        const ingredients = {...this.state.ingredients}
        if(ingredients[type] < 1) return;
        ingredients[type] -= 1;
        const price = this.state.totalPrice - INGREDIENT_PRICING[type];
        this.setState({
            ingredients: ingredients,
            totalPrice: price
        });
        this.updatePurchaseState(ingredients);
    }

    updatePurchaseState = (ingredients) => {
        const sum = Object.keys(ingredients).map(x=>ingredients[x]).reduce((sum, y) => sum+y, 0);
        this.setState({purchasable: sum>0});
    }

    purchaseHandler = () => {
        this.setState({purchasing:true});
    }

    render() {
        return (
            <Fragment>
                <OrderSummary ingredients={this.state.ingredients} purchasing={this.state.purchasing}/>
                <Burger ingredients={this.state.ingredients}/>
                <BuildControls 
                    ingredients={this.state.ingredients}
                    ingredientAdded={this.addIngredientHandler} 
                    ingredientRemoved={this.removeIngredientHandler}
                    price={this.state.totalPrice}
                    purchasable={this.state.purchasable}
                    purchaseHandler={this.purchaseHandler}
                />
            </Fragment>
        )
    }
}

export default BurgerBuilder;