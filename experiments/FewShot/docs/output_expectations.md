# Output Expectations

Any strings from the original story representing names of people, restaurants, food, etc.
should be placed within quotes, as in *"Allie"*, *"the waiter"*, *"miso soup"*, etc.


## Predicates:

`restaurant/1`  
`customer/1`  
`person/1`
`food/1`  
`waiter/1`  
`beverage/1`  
`host/1`
`cook/1`  

When the customers form a group referred to as *they* or something similar, and they perform an action like *enter* together or when the food/drinks is a collection of dishes/drinks ordered at the same time without a distinction on whom out of a group of customers will consume it (e.g., dish to share, for the whole table), then also use the predicate:

`member/2` - `member(X, Y)` means that item `X (person or dish)` is part of group `Y`.


`story_step(0..n)` --> this can be computed from the `st_obs` and `st_hpd`, so it is not as necessary

`st_obs(Fluent, true/false, I)` 
	where 
        - Fluent is one of the options listed at the bottom of this file
        - the second parameter is either the constant true or false, and 
        - `I` is a time step from 0 on (up to n inclusively)
`st_hpd(Action, true, I)`
	where 
        - Action is one of the options listed at the bottom of this file
        - the second parameter is either the constant true, and 
        - `I` is a time step from 0 on (up to n inclusively)
		  
`st_hpd(Action, false)` 
	where Action is an action that does not occur at any time step in the story
		  
`st_next(I1, I2)` - story steps `I1` and `I2` represent consecutive time steps in real time. This predicate is usually used in exceptional scenarios when the customer complains. If the complaint occurs at story step `I`, then add a fact saying `st_next(I-1, I).`  **It is a must-have in such stories**

		  

## Constants:
	
t - represents the table  
b - represents the bill  
r - represents the restaurant if the restaurant is not named in the story  
w - represents the waiter if the waiter is not named in the story  
f - represents an order consisting of several dishes  	  
tip - represents the tip  
		  
	  
## Fluents: (i.e., items that can be specified using `st_obs`)

- **`in(C, R)`** – Customer `C` is in restaurant `R`
- **`welcomed(C)`** – Customer `C` has been welcomed by the host/waiter
- **`at_l(X, L)`** – Thing or person `X` is at location `L`
- **`sitting(P)`** – Person `P` is sitting
- **`standing_by(P, L)`** – Person `P` is standing by location `L` (i.e., next to the table)
- **`holding(P, T)`** – Person `P` is holding thing `T`
- **`hungry(C)`** – Customer `C` is hungry
- **`paid(B)`** – Bill `B` has been paid
- **`open(R)`** – Restaurant `R` is open
- **`informed(P1, S, P2)`** – Person `P1` has transmitted information `S` to person `P2`
- **`bill_generated(C, B)`** – Bill `B` has been generated for customer `C`
- **`food_prepared(Ck, F, W)`** – Cook `Ck` has prepared food `F` for waiter `W` (i.e., requested by waiter `W`)
- **`available(F, R)`** – Food/dish `F` is available at restaurant `R`
- **`served(C)`** – Customer `C` has been served
- **`menu_read(C)`** – Customer `C` has read the menu


## Actions (Specifiable using `st_hpd`)

- **`enter(P, R)`** – Person `P` enters restaurant `R`
- **`greet(P, C)`** – Person `P` greets customer `C` (`P` can be a host or waiter)
- **`lead_to(P, C, L)`** – Person `P` leads customer `C` to location `L` (e.g., to a table)
- **`move(P, L1, L2)`** – Person `P` moves from location `L1` to location `L2`
- **`sit(P)`** – Person `P` sits down
- **`pick_up(P, T, L)`** – Person `P` picks up thing `T` from location `L` (e.g., a customer picks up the menu from the table)
- **`read_menu(P)`** – Person `P` reads the menu
- **`put_down(P, T, L)`** – Person `P` puts down thing `T` at location `L` (e.g., a customer places the menu back on the table)
- **`order(P, X, W)`** – Person `P` orders food/drink `X` from waiter `W`
- **`order_for(P1, P2, X, W)`** – Person `P1` orders food/drink `X` for person `P2` via waiter `W`
- **`prepare(Ck, F, W)`** – Cook `Ck` prepares food/dish `F` requested by waiter `W`
- **`eat(P, F)`** – Person `P` eats food/dish `F`
- **`drink(P, D)`** – Person `P` drinks beverage `D`
- **`request(P1, T, P2)`** – Person `P1` requests thing `T` (which can be an object or action) from person `P2`
- **`read_bill(P)`** – Person `P` reads the bill/check
- **`pay(P, B)`** – Person `P` pays bill `B`
- **`pay(P, T)`** – Person `P` pays tip `T`
- **`stand_up(P)`** – Person `P` stands up
- **`leave(P)`** – Person `P` leaves the restaurant
- **`order(P)`** – Person `P` orders (typically used in the negative to indicate that `P` does **not** order anything)
- **`complain(C, W)`** – Customer `C` complains to waiter `W`
- **`cancel_bill(P)`** – Person `P` (e.g., waiter or owner) cancels the bill

### These actions may not be actually mentioned in a story:
**`make_unavailable(F, R)`** - food/dish `F` becomes unavailable at restaurant `R` (by an external event)  
**interference** - an interference in the communication between two actors has occurred


