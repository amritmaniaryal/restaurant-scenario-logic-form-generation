# Gemini_evaluated

## Summary

- Total common: 100
- Exact matches: 0
- Partial matches: 100
- Accuracy: 0.0

---

## Story #26 — Partial Match (Similarity: 0.0000)

**Story:** 

### Predicted
```clingo
restaurant("vegetarian restaurant"). customer("Nicole"). food("lentil soup"). waiter("The waitress"). st_hpd(enter("Nicole", "vegetarian restaurant"), true, 0). st_hpd(order("Nicole", "lentil soup", "The waitress"), true, 1). st_hpd(put_down("The waitress", "lentil soup", t), true, 2). st_hpd(eat("Nicole", "lentil soup"), true, 3). st_hpd(leave("Nicole"), true, 4).
```

### Ground Truth
```clingo
restaurant(veg_r). customer(nicole). food(lentil_soup). waiter(waitress). story_step(0..4). st_hpd(enter(nicole, veg_r), true, 0). st_hpd(order(nicole, lentil_soup, waitress), true, 1). st_hpd(put_down(waitress, lentil_soup, t), true, 2). st_hpd(eat(nicole, lentil_soup), true, 3). st_hpd(leave(nicole), true, 4).
```

---

## Story #29 — Partial Match (Similarity: 0.0000)

**Story:** 

### Predicted
```clingo
restaurant("vegetarian restaurant"). customer("Nicole"). food("lentil soup"). waiter("the waitress"). st_hpd(enter("Nicole", "vegetarian restaurant"), true, 0). st_hpd(order("Nicole", "lentil soup", "the waitress"), true, 1). st_hpd(put_down("the waitress", "lentil soup", t), true, 2). st_hpd(cancel_bill("the waitress"), true, 2). st_hpd(eat("Nicole", "lentil soup"), true, 3). st_hpd(leave("Nicole"), true, 4).
```

### Ground Truth
```clingo
restaurant(veg_r). customer(nicole). person(owner). food(lentil_soup). waiter(waitress). story_step(0..5). st_hpd(enter(nicole, veg_r), true, 0). st_hpd(order(nicole, lentil_soup, waitress), true, 1). st_hpd(pay(owner, b), true, 2). st_hpd(put_down(waitress, lentil_soup, t), true, 3). st_hpd(eat(nicole, lentil_soup), true, 4). st_hpd(leave(nicole), true, 5).
```

---

## Story #30 — Partial Match (Similarity: 0.0000)

**Story:** 

### Predicted
```clingo
restaurant("vegetarian restaurant"). customer("Nicole"). food("lentil soup"). food("miso soup"). waiter("the waitress"). st_hpd(enter("Nicole", "vegetarian restaurant"), true, 0). st_hpd(order("Nicole", "lentil soup", "the waitress"), true, 1). st_hpd(put_down("the waitress", "miso soup", t), true, 2).
```

### Ground Truth
```clingo
restaurant(veg_r). customer(nicole). person(owner). food(lentil_soup). food(miso_soup). waiter(waitress). story_step(0..2). st_hpd(enter(nicole, veg_r), true, 0). st_hpd(order(nicole, lentil_soup, waitress), true, 1). st_hpd(put_down(waitress, miso_soup, t), true, 2).
```

---

## Story #31 — Partial Match (Similarity: 0.0000)

**Story:** 

### Predicted
```clingo
restaurant("vegetarian restaurant"). customer("Nicole"). food("lentil soup"). food("miso soup"). waiter("the waitress"). st_hpd(enter("Nicole", "vegetarian restaurant"), true, 0). st_hpd(order("Nicole", "lentil soup", "the waitress"), true, 1). st_hpd(put_down("the waitress", "miso soup", t), true, 2). st_hpd(eat("Nicole", "miso soup"), true, 3).
```

### Ground Truth
```clingo
restaurant(veg_r). customer(nicole). person(owner). food(lentil_soup). food(miso_soup). waiter(waitress). story_step(0..4). st_hpd(enter(nicole, veg_r), true, 0). st_hpd(order(nicole, lentil_soup, waitress), true, 1). st_hpd(put_down(waitress, miso_soup, t), true, 2). stop_activity(nicole, 3). next_st(2, 3). st_hpd(eat(nicole, miso_soup), true, 4).
```

---

## Story #32 — Partial Match (Similarity: 0.0000)

**Story:** 

### Predicted
```clingo
restaurant("vegetarian restaurant"). customer("Nicole"). food("lentil soup"). waiter("the waitress"). st_hpd(enter("Nicole", "vegetarian restaurant"), true, 0). st_hpd(order("Nicole", "lentil soup", "the waitress"), true, 1). st_hpd(put_down("the waitress", "lentil soup", t), true, 2). st_hpd(pay("Nicole", b), true, 3). st_hpd(read_bill("Nicole"), false).
```

### Ground Truth
```clingo
restaurant(veg_r). customer(nicole). person(owner). food(lentil_soup). waiter(waitress). story_step(0..3). st_hpd(enter(nicole, veg_r), true, 0). st_hpd(order(nicole, lentil_soup, waitress), true, 1). st_hpd(put_down(waitress, miso_soup, t), true, 2). st_hpd(pay(nicole, b), true, 3). next_st(2, 3).
```

---

## Story #64 — Partial Match (Similarity: 0.0000)

**Story:** 

### Predicted
```clingo
restaurant(r). customer(c_group). member("Penny", c_group). member("her friend", c_group). waiter(w). st_hpd(enter(c_group, r), true, 0). st_hpd(sit(c_group), true, 1). st_hpd(read_menu(c_group), true, 2). st_hpd(order(c_group, f, w), true, 3). st_hpd(eat(c_group, f), true, 4).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer(they). person("Penny"). person("her friend"). member("Penny", they). member("her friend", they). food("food"). story_step(0..5). st_hpd(enter(they, "the restaurant"), true, 0). st_hpd(sit(they), true, 1). st_hpd(read_menu(they), true, 3). st_hpd(order(they, "food", w), true, 4). st_hpd(eat(they, "food"), true, 5).
```

---

## Story #24 — Partial Match (Similarity: 0.0357)

**Story:** 

### Predicted
```clingo
restaurant(r). customer("Jasper"). customer("Frank"). food("roast beef"). beverage("coffee"). waiter(w). st_hpd(order("Jasper", "roast beef", w), true, 0). st_hpd(order("Jasper", "coffee", w), true, 0). st_hpd(put_down(w, "roast beef", t), true, 1). st_hpd(put_down(w, "coffee", t), true, 1). st_hpd(eat("Jasper", "roast beef"), true, 2). st_hpd(eat("Frank", "roast beef"), true, 2). st_hpd(drink("Jasper", "coffee"), true, 2). st_hpd(pay("Jasper", b), false). st_hpd(pay("Frank", b), true, 3).
```

### Ground Truth
```clingo
restaurant("a restaurant"). customer(they). member("Jasper", they). member("Frank", they). food(f). member("roast beef", f). member(coffee, f). waiter(w). story_step(0..4). st_hpd(enter(they, "a restaurant"), true, 0). st_hpd(order_for("Jasper", they, f, w), true, 1). st_hpd(put_down(w, f, t), true, 2). st_hpd(eat(they, f), true, 3). st_hpd(pay("Jasper", b), false, 4). st_hpd(pay("Frank", b), true, 4).
```

---

## Story #71 — Partial Match (Similarity: 0.0385)

**Story:** 

### Predicted
```clingo
restaurant("bistro"). customer("Michael"). food("the daily special"). beverage("a glass of water"). waiter("a waitress"). st_hpd(enter("Michael", "bistro"), true, 0). st_hpd(lead_to("a waitress", "Michael", t), true, 1). st_hpd(order("Michael", "the daily special", "a waitress"), true, 2). st_hpd(order("Michael", "a glass of water", "a waitress"), true, 2). st_hpd(put_down("a waitress", "the daily special", t), true, 3). st_hpd(put_down("a waitress", "a glass of water", t), true, 3). st_hpd(eat("Michael", "the daily special"), true, 4). st_hpd(request("Michael", b, "a waitress"), true, 5).
```

### Ground Truth
```clingo
restaurant("the bistro"). customer("Michael"). food("daily special"). beverage("water"). waiter("the waitress"). st_hpd(enter("Michael", "the bistro"), true, 0). st_hpd(lead_to("the host", "Michael", t), true, 1). st_hpd(order("Michael", "daily special", "the waitress"), true, 2). st_hpd(order("Michael", "water", "the waitress"), true, 2). st_hpd(put_down("the waitress", "daily special", t), true, 3). st_hpd(put_down("the waitress", "water", t), true, 3). st_hpd(eat("Michael", "daily special"), true, 4). st_hpd(drink("Michael", "water"), true, 4). st_hpd(request("Michael", b, "the waitress"), true, 5).
```

---

## Story #27 — Partial Match (Similarity: 0.0435)

**Story:** 

### Predicted
```clingo
restaurant("vegetarian restaurant"). customer("Nicole"). customer("Sam"). food("lentil soup"). food("miso soup"). waiter(w). st_hpd(enter("Nicole", "vegetarian restaurant"), true, 0). st_hpd(enter("Sam", "vegetarian restaurant"), true, 0). st_hpd(order("Nicole", "lentil soup", w), true, 1). st_hpd(order("Sam", "miso soup", w), true, 2). st_hpd(eat("Nicole", "lentil soup"), true, 3). st_hpd(eat("Sam", "miso soup"), true, 3).
```

### Ground Truth
```clingo
restaurant(veg_r). customer(nicole). customer(sam). food(lentil_soup). food(miso_soup). waiter(w). story_step(0..3). st_hpd(enter(nicole, veg_r), true, 0). st_hpd(enter(sam, veg_r), true, 0). st_hpd(order(nicole, lentil_soup, waitress), true, 1). st_hpd(order(sam, miso_soup, waitress), true, 2). st_hpd(eat(nicole, lentil_soup), true, 3). st_hpd(eat(sam, miso_soup), true, 3).
```

---

## Story #28 — Partial Match (Similarity: 0.0435)

**Story:** 

### Predicted
```clingo
restaurant("RRGrill restaurant"). customer("Andy"). food("soup"). waiter("the waiter"). st_obs(hungry("Andy"), true, 0). st_obs(open("RRGrill restaurant"), true, 1). st_hpd(enter("Andy", "RRGrill restaurant"), true, 2). st_hpd(greet("the waiter", "Andy"), true, 3). st_hpd(lead_to("the waiter", "Andy", t), true, 3). st_hpd(order("Andy", "soup", "the waiter"), true, 4). st_hpd(eat("Andy", "soup"), true, 5). st_hpd(pay("Andy", b), true, 6). st_hpd(leave("Andy"), true, 7).
```

### Ground Truth
```clingo
restaurant("RRGrill"). customer(andy). food(soup). waiter("the waiter"). story_step(0..4). st_hpd(enter(andy, "RRGrill"), true, 0). st_hpd(greet("the waiter", andy), true, 1). st_hpd(lead_to("the waiter", andy, t), true, 2). st_hpd(order(andy, soup, "the waiter"), true, 3). st_hpd(eat(andy, soup), true, 4). st_hpd(pay(andy, b), true, 5). st_hpd(leave(andy), true, 6).
```

---

## Story #13 — Partial Match (Similarity: 0.0500)

**Story:** 

### Predicted
```clingo
restaurant("local restaurant"). customer(c_group). member("Judy", c_group). member("Alex", c_group). member("Zoe", c_group). food("fish and chips"). waiter(w). st_hpd(read_menu("Judy"), true, 0). st_obs(sitting(c_group), true, 1). st_hpd(order(c_group, "fish and chips", w), true, 2).
```

### Ground Truth
```clingo
restaurant("a local restaurant"). person("Judy"). person("Alex"). person("Zoe"). customer("they"). member("Judy", "they"). member("Alex", "they"). member("Zoe", "they"). food("fish and chips"). story_step(0..1). st_obs(sitting("they"), true, 0). st_hpd(order("they", "fish and chips", w), true, 1).
```

---

## Story #77 — Partial Match (Similarity: 0.0526)

**Story:** 

### Predicted
```clingo
restaurant(r). customer(c_group). member("Karl", c_group). member("his wife", c_group). waiter("the waiter"). st_hpd(enter(c_group, r), true, 0). st_hpd(sit(c_group), true, 1). st_hpd(order(c_group), false). st_hpd(leave(c_group), true, 2).
```

### Ground Truth
```clingo
restaurant("new restaurant"). waiter("the waiter"). customer(they). person("Karl"). person("his wife"). member("Karl", they). member("his wife", they). waiter(w). st_obs(sitting(they), true, 0). st_hpd(served(they), false, 1). st_hpd(leave(they), true, 2).
```

---

## Story #90 — Partial Match (Similarity: 0.0588)

**Story:** 

### Predicted
```clingo
restaurant(r). customer(c_group). member("I", c_group). food("bread"). food(f). member("salmon", f). member("asparagus", f). st_hpd(enter(c_group, r), true, 0). st_hpd(eat(c_group, "bread"), true, 1). st_hpd(eat("I", f), true, 2).
```

### Ground Truth
```clingo
restaurant("a restaurant"). customer("My family"). customer("I"). food("bread"). food("salmon and asparagus"). st_hpd(enter("My family", "a restaurant"), true, 0). st_hpd(eat("My family", "bread"), true, 1). st_hpd(eat("I", "salmon and asparagus"), true, 1).
```

---

## Story #67 — Partial Match (Similarity: 0.0625)

**Story:** 

### Predicted
```clingo
restaurant("quiet Italian restaurant"). customer(c_group). member("Maria", c_group). member("Leo", c_group). beverage("a bottle of red wine"). food("two pasta dishes"). waiter("the waiter"). st_hpd(enter(c_group, "quiet Italian restaurant"), true, 0). st_hpd(lead_to("the waiter", c_group, t), true, 1). st_hpd(order(c_group, "a bottle of red wine", "the waiter"), true, 2). st_hpd(put_down("the waiter", "a bottle of red wine", t), true, 3). st_hpd(order(c_group, "two pasta dishes", "the waiter"), true, 4). st_hpd(eat(c_group, "two pasta dishes"), true, 5). st_hpd(drink(c_group, "a bottle of red wine"), true, 5). st_hpd(pay(c_group, b), true, 6). st_hpd(leave(c_group), true, 7).
```

### Ground Truth
```clingo
restaurant("quiet Italian restaurant"). customer(they). person("Maria"). person("Leo"). member("Maria", they). member("Leo", they). beverage("red wine"). food("pasta dishes"). waiter("the waiter"). story_step(0..7). st_hpd(enter(they, "quiet Italian restaurant"), true, 0). st_hpd(lead_to("the waiter", they, t), true, 1). st_hpd(order(they, "red wine", "the waiter"), true, 2). st_hpd(put_down("the waiter", "red wine", t), true, 3). st_hpd(order(they, "pasta dishes", "the waiter"), true, 4). st_hpd(eat(they, "pasta dishes"), true, 5). st_hpd(drink(they, "red wine"), true, 5). st_hpd(pay(they, b), true, 6). st_hpd(leave(they), true, 7).
```

---

## Story #76 — Partial Match (Similarity: 0.0769)

**Story:** 

### Predicted
```clingo
restaurant("Allston Diner"). customer(c_group). food("large, hearty breakfast meals"). st_hpd(enter(c_group, "Allston Diner"), true, 0). st_hpd(eat(c_group, "large, hearty breakfast meals"), true, 1).
```

### Ground Truth
```clingo
restaurant("Allston Diner"). customer(we). person("our son"). customer("a friend"). member("our son", we). food("breakfast meals"). st_hpd(enter(we, "Allston Diner"), true, 0). st_hpd(eat(we, "breakfast meals"), true, 1). st_hpd(eat("a friend", "breakfast meals"), true, 1).
```

---

## Story #34 — Partial Match (Similarity: 0.0833)

**Story:** 

### Predicted
```clingo
restaurant("RRGrill restaurant"). customer("Andy"). st_obs(hungry("Andy"), true, 0). st_hpd(enter("Andy", "RRGrill restaurant"), true, 1). st_obs(open("RRGrill restaurant"), true, 1). st_obs(available(t, "RRGrill restaurant"), false, 2). st_obs(available(t, "RRGrill restaurant"), true, 3).
```

### Ground Truth
```clingo
restaurant("RRGrill"). customer("Andy"). story_step(0..2). st_hpd(enter("Andy", "RRGrill"), true, 0). st_obs(table_available, false, 1). st_hpd(wait("Andy"), true, 1). st_hpd(free_table, true, 2).
```

---

## Story #35 — Partial Match (Similarity: 0.0833)

**Story:** 

### Predicted
```clingo
restaurant("RRGrill restaurant"). customer("Andy"). st_obs(hungry("Andy"), true, 0). st_hpd(enter("Andy", "RRGrill restaurant"), true, 1). st_obs(open("RRGrill restaurant"), true, 1). st_obs(available(t, "RRGrill restaurant"), false, 2). st_hpd(leave("Andy"), true, 3).
```

### Ground Truth
```clingo
restaurant("RRGrill"). customer("Andy"). story_step(0..2). st_hpd(enter("Andy", "RRGrill"), true, 0). st_obs(table_available, false, 1). stop_activity("Andy", 1). st_hpd(leave("Andy"), true, 2).
```

---

## Story #83 — Partial Match (Similarity: 0.0833)

**Story:** 

### Predicted
```clingo
restaurant("the diner"). customer(c_group). waiter("the waitress"). st_hpd(sit(c_group), true, 0). st_hpd(greet("the waitress", c_group), false). st_hpd(stand_up(c_group), true, 1). st_hpd(order(c_group, f, "the waitress"), true, 2).
```

### Ground Truth
```clingo
restaurant("diner"). customer("the couple"). waiter("the waitress"). st_hpd(sit("the couple"), true, 0). st_hpd(greet("the waitress", "the couple"), false). st_hpd(stand_up("the couple"), true, 1).
```

---

## Story #70 — Partial Match (Similarity: 0.0870)

**Story:** 

### Predicted
```clingo
restaurant("pizzeria"). customer(c_group). food("a large pepperoni pizza"). beverage("a pitcher of soda"). waiter("the waiter"). st_hpd(enter(c_group, "pizzeria"), true, 0). st_hpd(lead_to("the waiter", c_group, t), true, 1). st_hpd(order(c_group, "a large pepperoni pizza", "the waiter"), true, 2). st_hpd(order(c_group, "a pitcher of soda", "the waiter"), true, 2). st_hpd(put_down("the waiter", "a large pepperoni pizza", t), true, 3). st_hpd(put_down("the waiter", "a pitcher of soda", t), true, 3). st_hpd(eat(c_group, "a large pepperoni pizza"), true, 4). st_hpd(drink(c_group, "a pitcher of soda"), true, 4).
```

### Ground Truth
```clingo
restaurant("pizzeria"). customer("The Jackson family"). food("large pepperoni pizza"). beverage("pitcher of soda"). waiter("the waiter"). st_hpd(enter("The Jackson family", "pizzeria"), true, 0). st_hpd(lead_to("the waiter", "The Jackson family", t), true, 1). st_hpd(order("The Jackson family", "large pepperoni pizza", "the waiter"), true, 2). st_hpd(order("The Jackson family", "pitcher of soda", "the waiter"), true, 2). st_hpd(put_down("the waiter", "large pepperoni pizza", t), true, 3). st_hpd(put_down("the waiter", "pitcher of soda", t), true, 3). st_hpd(eat("The Jackson family", "large pepperoni pizza"), true, 4).
```

---

## Story #45 — Partial Match (Similarity: 0.0909)

**Story:** 

### Predicted
```clingo
restaurant(r). customer(c_group). waiter(w). st_obs(sitting(c_group), true, 0). st_hpd(order(c_group), false). st_hpd(leave(c_group), true, 1).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer("group of friends"). waiter(w). story_step(0..2). st_obs(sitting("group of friends"), true, 0). st_hpd(served("group of friends"), false). st_hpd(leave("group of friends"), true, 1).
```

---

## Story #96 — Partial Match (Similarity: 0.0909)

**Story:** 

### Predicted
```clingo
restaurant("fast food restaurant"). customer(c_group). member("Dina", c_group). member("a friend", c_group). food("fries"). waiter(w). st_hpd(in(c_group, "fast food restaurant"), true, 0). st_hpd(order(c_group, "fries", w), true, 1). st_hpd(pay("Dina", b), true, 2). st_hpd(pay("a friend", b), true, 2). st_hpd(eat("Dina", "fries"), true, 3).
```

### Ground Truth
```clingo
restaurant("fast food restaurant"). customer(they). person("Dina"). person("a friend"). member("Dina", they). member("a friend", they). food("fries"). st_obs(in("Dina", "fast food restaurant"), true, 0). st_obs(hungry("Dina"), false, 1). st_hpd(order(they, "fries", w), true, 2). st_hpd(pay("Dina", b), true, 3). st_hpd(pay("a friend", b), true, 3). st_hpd(eat("Dina", "fries"), true, 4).
```

---

## Story #19 — Partial Match (Similarity: 0.0938)

**Story:** 

### Predicted
```clingo
restaurant(r). customer("Brand"). beverage("whiskey with Pepsi, but no ice"). food(f1). member("Pyrogies", f1). member("sausage cooked in sauerkraut", f1). food("a large bowl of borscht"). waiter("the waiter"). st_obs(sitting("Brand"), true, 0). st_hpd(pick_up("Brand", menu, t), true, 1). st_hpd(order("Brand", "whiskey with Pepsi, but no ice", "the waiter"), true, 2). st_hpd(order("Brand", f1, "the waiter"), true, 2). st_hpd(put_down("the waiter", "whiskey with Pepsi, but no ice", t), true, 3). st_hpd(put_down("the waiter", f1, t), true, 4). st_hpd(request("Brand", "a large bowl of borscht", "the waiter"), true, 5). st_hpd(eat("Brand", f1), true, 6). st_hpd(put_down("the waiter", "a large bowl of borscht", t), true, 7).
```

### Ground Truth
```clingo
restaurant(r). customer("Brand"). beverage("whiskey with Pepsi, no ice"). food(f). member(pyrogies, f). member("sausage in sauerkraut", f). food(borscht). waiter("the waiter"). story_step(0..9). st_hpd(sit("Brand"), true, 0). st_hpd(pick_up("Brand", m, t), true, 1). st_hpd(order("Brand", "whiskey with Pepsi, no ice", "the waiter"), true, 2). st_hpd(order("Brand", f, "the waiter"), true, 3). st_hpd(put_down("the waiter", "whiskey with Pepsi, no ice"), t), true, 4). st_hpd(put_down("the waiter", f, t), true, 5). st_hpd(order("Brand", borscht, "the waiter"), true, 6). st_hpd(move("the waiter", t, kitchen), true, 7). st_hpd(eat("Brand", f), true, 8). st_hpd(put_down("the waiter", borscht, t), true, 9).
```

---

## Story #25 — Partial Match (Similarity: 0.1111)

**Story:** 

### Predicted
```clingo
restaurant(r). customer("I"). customer("Uncle Chipperton"). waiter("the head-waiter"). food("a capital dinner"). st_hpd(enter("I", r), true, 0). st_hpd(sit("I"), true, 1). st_hpd(eat("I", "a capital dinner"), true, 2). st_hpd(enter("Uncle Chipperton", r), true, 3). st_hpd(pay("Uncle Chipperton", b), true, 4).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer("I"). waiter("head-waiter") food("capital dinner"). person("Uncle Chipperton"). story_step(0..5). st_hpd(enter("I", "the restaurant"), true, 0). st_hpd(sit("I"), true, 1). st_hpd(put_down("head-waiter", "capital dinner", t), true, 2). st_hpd(eat("I", "capital dinner"), true, 3). st_hpd(enter("Uncle Chipperton", "the restaurant"), true, 4). st_hpd(pay("Uncle Chipperton", b), true, 5).
```

---

## Story #33 — Partial Match (Similarity: 0.1111)

**Story:** 

### Predicted
```clingo
restaurant("RRGrill restaurant"). customer("Andy"). st_obs(hungry("Andy"), true, 0). st_hpd(enter("Andy", "RRGrill restaurant"), true, 1). st_obs(open("RRGrill restaurant"), true, 1). st_obs(available(t, "RRGrill restaurant"), false, 2).
```

### Ground Truth
```clingo
restaurant("RRGrill"). customer("Andy"). story_step(0..1). st_hpd(enter("Andy", "RRGrill"), true, 0). st_obs(table_available, false, 1).
```

---

## Story #74 — Partial Match (Similarity: 0.1154)

**Story:** 

### Predicted
```clingo
restaurant("Italian restaurant"). customer(c_group). member("Lisa", c_group). member("Mark", c_group). food("lasagna"). food("chicken parmesan"). beverage("a bottle of wine"). waiter(w). st_hpd(enter(c_group, "Italian restaurant"), true, 0). st_hpd(sit(c_group), true, 1). st_hpd(order("Lisa", "lasagna", w), true, 2). st_hpd(order("Mark", "chicken parmesan", w), true, 2). st_hpd(drink(c_group, "a bottle of wine"), true, 3).
```

### Ground Truth
```clingo
restaurant("Italian restaurant"). customer("Lisa"). customer("Mark"). customer(they). member("Lisa", they). member("Mark", they). food("lasagna"). food("chicken parmesan"). beverage("wine"). st_hpd(enter(they, "Italian restaurant"), true, 0). st_obs(sitting(they), true, 1). st_hpd(order("Lisa", "lasagna", "the waiter"), true, 2). st_hpd(order("Mark", "chicken parmesan", "the waiter"), true, 2). st_hpd(eat("Lisa", "lasagna"), true, 3). st_hpd(eat("Mark", "chicken parmesan"), true, 3). st_hpd(drink(they, "wine"), true, 3).
```

---

## Story #47 — Partial Match (Similarity: 0.1176)

**Story:** 

### Predicted
```clingo
restaurant(r). customer("Gary"). food("a steak"). food("a small cake"). waiter("the waiter"). st_hpd(enter("Gary", r), true, 0). st_hpd(order("Gary", "a steak", "the waiter"), true, 1). st_hpd(eat("Gary", "a steak"), true, 2). st_hpd(put_down("the waiter", "a small cake", t), true, 3). st_hpd(pay("Gary", tip), true, 4).
```

### Ground Truth
```clingo
restaurant("a restaurant"). customer("Gary"). food("steak"). food("cake"). waiter("the waiter"). story_step(0..3). st_hpd(order("Gary", "steak", "the waiter"), true, 0). st_hpd(eat("Gary", "steak"), true, 1). st_hpd(put_down("the waiter", "cake", t), true, 2). st_hpd(pay("Gary", tip), true, 3).
```

---

## Story #12 — Partial Match (Similarity: 0.1200)

**Story:** 

### Predicted
```clingo
restaurant("famous restaurant"). customer(c_group). member("I", c_group). member("my husband", c_group). food(f). member("escargot", f). member("lamb", f). member("savory salmon", f). member("creamy flan dessert", f). waiter(w). st_hpd(enter(c_group, "famous restaurant"), true, 0). st_hpd(sit(c_group), true, 1). st_hpd(read_menu(c_group), true, 2). st_hpd(order(c_group, f, w), true, 3).
```

### Ground Truth
```clingo
restaurant("a famous restaurant"). person("my husband"). person("I"). customer("we"). member("my husband", "we"). member("I", "we"). member("escargot", f). member("lamb", f). member("savory salmon", f). member("creamy flan dessert", f) story_step(0..3). st_hpd(enter("we", "a famous restaurant"), true, 0). st_obs(sitting("we"), true, 1). st_hpd(read_menu("we"), true, 2). st_hpd(order("we", f, w), true, 3).
```

---

## Story #22 — Partial Match (Similarity: 0.1250)

**Story:** 

### Predicted
```clingo
restaurant(r). customer("Andrew"). customer("Sebastian"). beverage("a bottle of wine"). waiter("the waiter"). st_obs(sitting("Andrew"), true, 0). st_hpd(enter("Sebastian", r), true, 1). st_hpd(sit("Sebastian"), true, 2). st_hpd(put_down("the waiter", "a bottle of wine", t), true, 3). st_hpd(drink("Andrew", "a bottle of wine"), true, 4). st_hpd(drink("Sebastian", "a bottle of wine"), true, 4). st_hpd(put_down("the waiter", menu, t), true, 5).
```

### Ground Truth
```clingo
restaurant("a restaurant"). customer("the men"). person("Andrew"). person("Sebastian"). member("Andrew", "the men"). member("Sebastian", "the men"). drink(wine). waiter("the waiter"). story_step(0..5). st_obs(in("Andrew", "a restaurant"), true, 0). st_obs(sitting("Andrew"), true, 0). st_hpd(enter("Sebastian", "a restaurant"), true, 1). st_hpd(sit("Sebastian"), true, 2). st_hpd(put_down("the waiter", wine, t), true, 3). st_hpd(drink("the men", wine), true, 4). st_hpd("the waiter", m, t), true, 5).
```

---

## Story #36 — Partial Match (Similarity: 0.1250)

**Story:** 

### Predicted
```clingo
restaurant("RRGrill restaurant"). customer("Andy"). person("Tom"). waiter("the waiter"). st_obs(hungry("Andy"), true, 0). st_obs(open("RRGrill restaurant"), true, 1). st_obs(paid(b), true, 1). st_hpd(enter("Andy", "RRGrill restaurant"), true, 2). st_hpd(lead_to("the waiter", "Andy", t), true, 3).
```

### Ground Truth
```clingo
restaurant("RRGrill"). customer("Andy"). person("Tom"). food("all the food"). waiter("the waitress"). story_step(0..2). st_hpd(enter("Andy", "RRGrill"), true, 0). st_hpd(lead_to("waitress", "Andy", t), true, 1). st_obs(informed("the waitress", "all the food", "Andy"), true, 2). st_hpd(pay("Tom", b), 2).
```

---

## Story #39 — Partial Match (Similarity: 0.1250)

**Story:** 

### Predicted
```clingo
restaurant("RRGrill restaurant"). customer("Andy"). waiter("the waiter"). st_obs(hungry("Andy"), true, 0). st_hpd(enter("Andy", "RRGrill restaurant"), true, 1). st_obs(open("RRGrill restaurant"), true, 1). st_hpd(lead_to("the waiter", "Andy", t), true, 2). st_hpd(sit("Andy"), true, 3). st_hpd(order("Andy"), false). st_hpd(leave("Andy"), true, 4).
```

### Ground Truth
```clingo
restaurant("RRGrill"). customer("Andy"). waiter("the waiter"). story_step(0..3). st_hpd(enter("Andy", "RRGrill"), true, 0). st_hpd(lead_to("the waiter", "Andy", t), true, 1). st_obs(sitting("Andy"), true, 2). st_stop_activity("Andy", 2). st_hpd(leave("Andy"), true, 3).
```

---

## Story #80 — Partial Match (Similarity: 0.1250)

**Story:** 

### Predicted
```clingo
restaurant("Genki Ya"). customer(c_group). member("I", c_group). member("my son", c_group). food(f). member("fish roe", f). member("two combo sashimi-sushi dishes", f). beverage("Japanese beers"). waiter(w). st_hpd(enter(c_group, "Genki Ya"), true, 0). st_hpd(order(c_group, f, w), true, 1). st_hpd(order(c_group, "Japanese beers", w), true, 1). st_hpd(eat(c_group, f), true, 2). st_hpd(drink(c_group, "Japanese beers"), true, 2).
```

### Ground Truth
```clingo
restaurant("Genki Ya"). customer(we). person("my son"). person("I"). member("my son", we). member("I", we). beverage("japanese beers"). food(f). member("fish roe", f). member("sashimi-sushi dishes", f). st_hpd(enter(we, "Genki Ya"), true, 0). st_hpd(eat(we, f), true, 2). st_hpd(drink(we, "japanese beers"), true, 2).
```

---

## Story #21 — Partial Match (Similarity: 0.1364)

**Story:** 

### Predicted
```clingo
restaurant(r). customer(c_group). member("Emanuel", c_group). member("Ingrid", c_group). beverage("wine"). food("gypsy shashlik"). waiter("the waiter"). st_hpd(put_down("the waiter", "wine", t), true, 0). st_hpd(read_menu("Emanuel"), true, 1). st_hpd(order_for("Emanuel", c_group, "gypsy shashlik", "the waiter"), true, 2). st_hpd(drink(c_group, "wine"), true, 3). st_hpd(put_down("the waiter", "gypsy shashlik", t), true, 4).
```

### Ground Truth
```clingo
restaurant(r). customer(they). member("Emanuel"). member("Ingrid"). drink(wine). food("gypsy shashlik"). waiter("the waiter"). story_step(0..5). st_hpd(put_down("the waiter", wine, t), true, 0). st_hpd(pick_up("Emanuel", m, t), true, 1). st_hpd(order_for("Emanuel", they, "gypsy shashlik", "the waiter"), true, 2). st_hpd(move("the waiter", t, kitchen), true, 3). st_hpd(drink(they, wine), true, 4). st_hpd(put_down("the waiter", "gypsy shashlik", t), true, 5).
```

---

## Story #51 — Partial Match (Similarity: 0.1429)

**Story:** 

### Predicted
```clingo
restaurant("pizzeria"). customer(c_group). member("Steve", c_group). member("his son", c_group). food("a large pepperoni pizza"). waiter("the waiter"). st_hpd(enter(c_group, "pizzeria"), true, 0). st_hpd(lead_to("the waiter", c_group, t), true, 1). st_hpd(order(c_group, "a large pepperoni pizza", "the waiter"), true, 2). st_hpd(eat(c_group, "a large pepperoni pizza"), true, 3). st_hpd(pay("Steve", b), true, 4).
```

### Ground Truth
```clingo
restaurant("pizzeria"). customer(they). person("Steve"). person("his son"). member("Steve", they). member("his son", they). food("large pepperoni pizza"). waiter("the waiter"). story_step(0..4). st_hpd(enter(they, "pizzeria"), true, 0). st_hpd(lead_to("the waiter", they, t), true, 1). st_hpd(order(they, "large pepperoni pizza", "the waiter"), true, 2). st_hpd(eat(they, "large pepperoni pizza"), true, 3). st_hpd(pay("Steve", b), true, 4).
```

---

## Story #53 — Partial Match (Similarity: 0.1429)

**Story:** 

### Predicted
```clingo
restaurant("family restaurant"). customer(c_group). member("Mr. Johnson", c_group). member("Mrs. Johnson", c_group). member("their son", c_group). food("steak"). food("salad"). food("pizza"). food(f). member("steak", f). member("salad", f). member("pizza", f). waiter("the waiter"). st_hpd(enter(c_group, "family restaurant"), true, 0). st_hpd(sit(c_group), true, 1). st_hpd(read_menu(c_group), true, 2). st_hpd(order("Mr. Johnson", "steak", "the waiter"), true, 3). st_hpd(order("Mrs. Johnson", "salad", "the waiter"), true, 3). st_hpd(order("their son", "pizza", "the waiter"), true, 3). st_hpd(put_down("the waiter", f, t), true, 4).
```

### Ground Truth
```clingo
restaurant("family restaurant"). person("Mr. Johnson"). person("Mrs. Johnson"). person("son"). customer("Johnson family"). member("Mr. Johnson", "Johnson family"). member("Mrs. Johnson", "Johnson family"). member("son", "Johnson family"). food("steak"). food("salad"). food("pizza"). waiter("the waiter"). story_step(0..4). st_hpd(enter("Johnson family", "family restaurant"), true, 0). st_obs(sitting("Johnson family"), true, 1). st_hpd(order("Mr. Johnson", "steak", "the waiter"), true, 2). st_hpd(order("Mrs. Johnson", "salad", "the waiter"), true, 2). st_hpd(order("son", "pizza", "the waiter"), true, 2). st_hpd(put_down("the waiter", "steak", t), true, 3). st_hpd(put_down("the waiter", "salad", t), true, 3). st_hpd(put_down("the waiter", "pizza", t), true, 3).
```

---

## Story #79 — Partial Match (Similarity: 0.1429)

**Story:** 

### Predicted
```clingo
restaurant("new steakhouse"). customer(c_group). food("huge cuts of meat"). waiter(w). st_hpd(enter(c_group, "new steakhouse"), true, 0). st_hpd(order(c_group, "huge cuts of meat", w), true, 1). st_hpd(put_down(w, "huge cuts of meat", t), true, 2). st_hpd(eat(c_group, "huge cuts of meat"), false). st_hpd(read_bill(c_group), true, 3).
```

### Ground Truth
```clingo
restaurant("new steakhouse"). customer("the couple"). food("huge cuts of meat"). st_obs(in("the couple", "new steakhouse"), true, 0). st_hpd(put_down(w, "huge cuts of meat", t), true, 1). st_hpd(eat("the couple", "huge cuts of meat"), true, 2). st_hpd(put_down(w, b, t), true, 3).
```

---

## Story #81 — Partial Match (Similarity: 0.1429)

**Story:** 

### Predicted
```clingo
restaurant("new Italian restaurant"). customer(c_group). member("Kathy", c_group). member("her friend", c_group). food("dinner"). st_hpd(enter(c_group, "new Italian restaurant"), true, 0). st_hpd(eat(c_group, "dinner"), true, 1).
```

### Ground Truth
```clingo
restaurant("new Italian restaurant"). customer(they). person("Kathy"). person("her friend"). member("Kathy", they). member("her friend", they). food("dinner"). st_hpd(enter(they, "new Italian restaurant"), true, 0). st_hpd(eat(they, "dinner"), true, 1).
```

---

## Story #89 — Partial Match (Similarity: 0.1429)

**Story:** 

### Predicted
```clingo
restaurant("Genki Ya"). customer(c_group). member("I", c_group). member("my son", c_group). food("sashimi"). st_hpd(enter(c_group, "Genki Ya"), true, 0). st_hpd(eat(c_group, "sashimi"), true, 1).
```

### Ground Truth
```clingo
restaurant("Genki Ya"). customer(we). person("my son"). person("me"). member("my son", we). member("me", we). food("sashimi"). st_hpd(enter(we, "Genki Ya"), true, 0). st_hpd(eat(we, "sashimi"), true, 1).
```

---

## Story #14 — Partial Match (Similarity: 0.1538)

**Story:** 

### Predicted
```clingo
restaurant("five-star restaurant"). customer("Samantha"). food(f). member("the barbecued veal chop with Asian slaw", f). member("Thai fried rice", f). waiter(w). st_obs(in("Samantha", "five-star restaurant"), true, 0). st_hpd(read_menu("Samantha"), true, 1). st_hpd(order("Samantha", f, w), true, 2).
```

### Ground Truth
```clingo
restaurant("a five-star restaurant"). customer("Samantha"). food("barbecued veal chop with Asian slaw and Thai fried rice"). story_step(0..2). st_obs(in("Samantha", "a five-star restaurant"), true, 0). st_hpd(read_menu("Samantha"), true, 1). st_hpd(order("Samantha", "barbecued veal chop with Asian slaw and Thai fried rice", w), true, 2).
```

---

## Story #87 — Partial Match (Similarity: 0.1538)

**Story:** 

### Predicted
```clingo
restaurant(r). customer("I"). food("wrong order"). waiter(w). st_hpd(enter("I", r), true, 0). st_hpd(put_down(w, "wrong order", t), true, 1). st_hpd(request("I", "return it", w), true, 2).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer("I"). food("wrong order"). st_hpd(enter("I", "the restaurant"), true, 0). st_hpd(order("I", f, w), true, 1). st_hpd(put_down(w, "wrong order", t), true, 2). st_hpd(request("I", pick_up(w, "burnt pizza", t), w), true, 3). st_next(2,3).
```

---

## Story #3 — Partial Match (Similarity: 0.1667)

**Story:** 

### Predicted
```clingo
restaurant(r). customer("Jill"). food("chicken"). waiter("the waiter"). st_hpd(enter("Jill", r), true, 0). st_hpd(lead_to(w, "Jill", t), true, 1). st_hpd(sit("Jill"), true, 2). st_hpd(order("Jill", "chicken", "the waiter"), true, 3). st_hpd(put_down("the waiter", "chicken", t), true, 4). st_hpd(eat("Jill", "chicken"), true, 5). st_hpd(request("Jill", b, "the waiter"), true, 6).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer("Jill"). food("chicken"). waiter("the waiter"). story_step(0..5). st_hpd(enter("Jill", "the restaurant"), true, 0). st_hpd(lead_to("the waiter", "Jill", t), true, 1). st_hpd(order("Jill", "chicken", "the waiter"), true, 2). st_hpd(put_down("the waiter", "chicken", t), true, 3). st_hpd(eat("Jill", "chicken"), true, 4). st_hpd(request("Jill", b, "the waiter"), true, 5).
```

---

## Story #99 — Partial Match (Similarity: 0.1667)

**Story:** 

### Predicted
```clingo
restaurant("new restaurant"). customer(c_group). food(f). food("tacos"). food("chicken tacos"). st_hpd(enter(c_group, "new restaurant"), true, 0). st_hpd(eat(c_group, f), true, 1).
```

### Ground Truth
```clingo
restaurant("new restaurant"). customer("The family"). food("different foods"). food("tacos"). st_hpd(enter("The family", "new restaurant"), true, 0). st_hpd(order("The family", "different foods", w), true, 1). st_hpd(eat("The family", "different foods"), true, 2).
```

---

## Story #38 — Partial Match (Similarity: 0.1765)

**Story:** 

### Predicted
```clingo
restaurant("RRGrill restaurant"). customer("Andy"). waiter("the waiter"). st_obs(hungry("Andy"), true, 0). st_hpd(enter("Andy", "RRGrill restaurant"), true, 1). st_obs(open("RRGrill restaurant"), true, 1). st_hpd(lead_to("the waiter", "Andy", t), true, 2). st_hpd(read_menu("Andy"), true, 3). st_hpd(order("Andy"), false). st_hpd(leave("Andy"), true, 4).
```

### Ground Truth
```clingo
restaurant("RRGrill"). customer("Andy"). food("nothing"). waiter("the waiter"). story_step(0..4). st_hpd(enter("Andy", "RRGrill"), true, 0). st_hpd(lead_to("the waiter", "Andy", t), true, 1). st_hpd(put_down("Andy", m, t), true, 2). st_stop_activity("Andy", 3). next_st(2, 3). st_hpd(leave("Andy"), true, 4).
```

---

## Story #61 — Partial Match (Similarity: 0.1765)

**Story:** 

### Predicted
```clingo
restaurant("quiet cafe"). customer(c_group). member("book club members", c_group). beverage("teas"). food("pastries"). waiter(w). st_hpd(enter(c_group, "quiet cafe"), true, 0). st_hpd(order(c_group, "teas", w), true, 1). st_hpd(order(c_group, "pastries", w), true, 1). st_hpd(eat(c_group, "pastries"), true, 2). st_hpd(drink(c_group, "teas"), true, 2).
```

### Ground Truth
```clingo
restaurant("quiet cafe"). customer("book club members"). food("pastries"). beverage("teas"). story_step(0..2). st_hpd(enter("book club members", "quiet cafe"), true, 0). st_hpd(order("book club members", "pastries", "the waiter"), true, 1). st_hpd(order("book club members", "teas", "the waiter"), true, 1). st_hpd(eat("book club members", "pastries"), true, 2). st_hpd(drink("book club members", "teas"), true, 2).
```

---

## Story #86 — Partial Match (Similarity: 0.1818)

**Story:** 

### Predicted
```clingo
restaurant("a diner"). customer("Samuel"). customer("John"). food("a hamburger without onions"). food("a hotdog"). waiter("the waiter"). st_obs(in("Samuel", "a diner"), true, 0). st_obs(in("John", "a diner"), true, 0). st_hpd(order("Samuel", "a hamburger without onions", "the waiter"), true, 1). st_hpd(put_down("the waiter", "a hotdog", t), true, 2). st_hpd(complain("Samuel", "the waiter"), true, 3). st_next(2, 3). st_hpd(put_down("the waiter", "a hamburger without onions", t), true, 4).
```

### Ground Truth
```clingo
restaurant("diner"). customer("Samuel"). customer("John"). food("hamburger without onions"). food("hotdog"). waiter("the waiter"). st_obs(in("Samuel", "diner"), true, 0). st_obs(in("John", "diner"), true, 0). st_hpd(order("Samuel", "hamburger without onions", "the waiter"), true, 1). st_hpd(put_down("the waiter", "hotdog", t), true, 2). st_hpd(complain("Samuel", "the waiter"), true, 3). st_next(2,3). st_hpd(put_down("the waiter", "hamburger without onions", t), true, 4).
```

---

## Story #15 — Partial Match (Similarity: 0.1875)

**Story:** 

### Predicted
```clingo
restaurant("fine restaurant"). customer("the villager"). food("one of the items on the list"). food("lettuce salad with several black olives on top"). waiter("the waiter"). st_hpd(enter("the villager", "fine restaurant"), true, 0). st_hpd(sit("the villager"), true, 1). st_hpd(read_menu("the villager"), true, 2). st_hpd(order("the villager", "one of the items on the list", "the waiter"), true, 3). st_hpd(put_down("the waiter", "lettuce salad with several black olives on top", t), true, 4).
```

### Ground Truth
```clingo
restaurant("a fine restaurant"). customer("the villager"). food("one of the items on the list"). food("lettuce salad with several black olives on top"). story_step(0..4). st_hpd(enter("the villager", "a fine restaurant"), true, 0). st_obs(sitting("the villager"), true, 1). st_hpd(pick_up("the villager", m, t), true, 2). st_hpd(order("the villager", "one of the items on the list", w), true, 3). st_hpd(put_down(w, "lettuce salad with several black olives on top", t), true, 4).
```

---

## Story #82 — Partial Match (Similarity: 0.1905)

**Story:** 

### Predicted
```clingo
restaurant(r). customer(c_group). member("Elmer", c_group). member("Emma", c_group). food("burgers"). food("fries"). beverage("milkshakes"). waiter(w). st_hpd(enter(c_group, r), true, 0). st_hpd(order(c_group, "burgers", w), true, 1). st_hpd(order(c_group, "milkshakes", w), true, 1). st_hpd(order("Elmer", "fries", w), true, 2).
```

### Ground Truth
```clingo
restaurant("new restaurant"). customer("the couple"). person("Elmer"). person("Emma"). member("Elmer", "the couple"). member("Emma", "the couple"). food("burgers"). food("fries"). beverage("milkshakes"). st_hpd(enter("the couple", "new restaurant"), true, 0). st_hpd(order("the couple", "burgers", w), true, 1). st_hpd(order("the couple", "milkshakes", w), true, 1). st_hpd(order("Elmer", "fries", w), true, 2).
```

---

## Story #2 — Partial Match (Similarity: 0.2000)

**Story:** 

### Predicted
```clingo
restaurant(r). customer("John"). food("steak"). waiter("the waiter"). st_hpd(enter("John", r), true, 0). st_hpd(lead_to("the waiter", "John", t), true, 1). st_hpd(sit("John"), true, 2). st_hpd(order("John", "steak", "the waiter"), true, 3). st_hpd(put_down("the waiter", "steak", t), true, 4). st_hpd(request("John", b, "the waiter"), true, 5). st_hpd(put_down("the waiter", b, t), true, 6). st_hpd(pay("John", b), true, 7). st_hpd(leave("John"), true, 8).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer("John"). food("steak"). waiter("the waiter"). story_step(0..6). st_hpd(enter("John", "the restaurant"), true, 0). st_hpd(lead_to("the waiter", "John", t), true, 1). st_hpd(order("John", "steak", "the waiter"), true, 2). st_hpd(request("John", b, "the waiter"), true, 3). st_hpd(put_down("the waiter", b, t), true, 4). st_pay(pay("John", b), true, 5). st_pay(leave("John"), true, 6).
```

---

## Story #37 — Partial Match (Similarity: 0.2000)

**Story:** 

### Predicted
```clingo
restaurant("RRGrill restaurant"). restaurant("Happy Pizza"). customer("Andy"). st_obs(hungry("Andy"), true, 0). st_obs(open("RRGrill restaurant"), false, 1). st_hpd(enter("Andy", "Happy Pizza"), true, 2).
```

### Ground Truth
```clingo
restaurant("RRGrill"). restaurant("Happy Pizza"). customer("Andy"). story_step(0..2). st_obs(closed("RRGrill"), true, 0). stop_activity("Andy", 1). st_hpd(move("Andy", "RRGrill", "Happy Pizza"), true, 2).
```

---

## Story #54 — Partial Match (Similarity: 0.2000)

**Story:** 

### Predicted
```clingo
restaurant("cafe"). customer("Sarah"). food("a chicken sandwich"). beverage("coffee"). waiter("The waitress"). st_hpd(enter("Sarah", "cafe"), true, 0). st_hpd(sit("Sarah"), true, 1). st_hpd(order("Sarah", "a chicken sandwich", "The waitress"), true, 2). st_hpd(order("Sarah", "coffee", "The waitress"), true, 2). st_hpd(put_down("The waitress", "a chicken sandwich", t), true, 3). st_hpd(put_down("The waitress", "coffee", t), true, 3). st_hpd(eat("Sarah", "a chicken sandwich"), true, 4). st_hpd(drink("Sarah", "coffee"), true, 4).
```

### Ground Truth
```clingo
restaurant("the cafe"). customer("Sarah"). food("chicken sandwich"). beverage("coffee"). waiter("the waitress"). story_step(0..4). st_hpd(enter("Sarah", "the cafe"), true, 0). st_hpd(sit("Sarah"), true, 1). st_hpd(order("Sarah", "chicken sandwich", "the waitress"), true, 2). st_hpd(put_down("the waitress", "chicken sandwich", t), true, 3). st_hpd(eat("Sarah", "chicken sandwich"), true, 4). st_hpd(drink("Sarah", "coffee"), true, 4).
```

---

## Story #52 — Partial Match (Similarity: 0.2105)

**Story:** 

### Predicted
```clingo
restaurant("seafood restaurant"). customer("David"). food("grilled salmon with vegetables"). waiter(w). st_hpd(enter("David", "seafood restaurant"), true, 0). st_hpd(lead_to(w, "David", t), true, 1). st_hpd(read_menu("David"), true, 2). st_hpd(order("David", "grilled salmon with vegetables", w), true, 3). st_hpd(put_down(w, "grilled salmon with vegetables", t), true, 4). st_hpd(eat("David", "grilled salmon with vegetables"), true, 5). st_hpd(pay("David", b), true, 6). st_hpd(leave("David"), true, 7).
```

### Ground Truth
```clingo
restaurant("seafood restaurant"). customer("David"). food("grilled salmon with vegetables"). waiter("the waiter"). st_hpd(enter("David", "seafood restaurant"), true, 0). st_hpd(lead_to("the waiter", "David", t), true, 1). st_hpd(order("David", "grilled salmon with vegetables", "the waiter"), true, 2). st_hpd(put_down("the waiter", "grilled salmon with vegetables", t), true, 3). st_hpd(eat("David", "grilled salmon with vegetables"), true, 4). st_hpd(pay("David", b), true, 5). st_hpd(leave("David"), true, 6).
```

---

## Story #75 — Partial Match (Similarity: 0.2105)

**Story:** 

### Predicted
```clingo
restaurant("new Sushi place"). customer(c_group). member("I", c_group). member("my husband", c_group). food(f). member("spicy tuna rolls", f). member("eel", f). waiter(w). st_hpd(enter(c_group, "new Sushi place"), true, 0). st_hpd(order(c_group, f, w), true, 1). st_hpd(eat(c_group, f), true, 2).
```

### Ground Truth
```clingo
restaurant("new Sushi place"). customer(we). person("I"). person("my husband"). member("I", we). member("my husband", we). food(f). member("spicy tuna rolls", f). member("eel", f). st_hpd(enter(we, "new Sushi place"), true, 0). st_hpd(order(we, f, w), true, 1). st_hpd(eat(we, f), true, 2).
```

---

## Story #69 — Partial Match (Similarity: 0.2222)

**Story:** 

### Predicted
```clingo
restaurant("sandwich shop"). customer(c_group). food("sandwiches"). waiter("the waiter"). st_hpd(enter(c_group, "sandwich shop"), true, 0). st_hpd(lead_to("the waiter", c_group, t), true, 1). st_hpd(order(c_group, "sandwiches", "the waiter"), true, 2). st_hpd(put_down("the waiter", "sandwiches", t), true, 3). st_hpd(eat(c_group, "sandwiches"), true, 4). st_hpd(pay(c_group, b), true, 5). st_hpd(leave(c_group), true, 6).
```

### Ground Truth
```clingo
restaurant("sandwich shop"). customer("group of coworkers"). food("sandwiches"). waiter("the waiter"). st_hpd(enter("group of coworkers", "sandwich shop"), true, 0). st_hpd(lead_to("the waiter", "group of coworkers", t), true, 1). st_hpd(order("group of coworkers", "sandwiches", "the waiter"), true, 2). st_hpd(put_down("the waiter", "sandwiches", t), true, 3). st_hpd(eat("group of coworkers", "sandwiches"), true, 4). st_hpd(pay("group of coworkers", b), true, 5). st_hpd(leave("group of coworkers"), true, 6).
```

---

## Story #95 — Partial Match (Similarity: 0.2222)

**Story:** 

### Predicted
```clingo
restaurant(r). person("Austin"). customer("a homeless man"). food("spare food"). food("a full meal"). waiter("the wait staff"). st_hpd(enter("a homeless man", r), true, 0). st_hpd(request("a homeless man", "spare food", "Austin"), true, 1). st_hpd(lead_to("Austin", "a homeless man", t), true, 2). st_hpd(put_down("the wait staff", "a full meal", t), true, 3). st_hpd(cancel_bill("Austin"), true, 4).
```

### Ground Truth
```clingo
restaurant("a restaurant"). customer("a homeless man"). waiter("wait staff"). person("Austin"). food("spare food"). food("full meal").  st_hpd(enter("a homeless man", "a restaurant"), true, 0). st_hpd(request("a homeless man", "spare food", "Austin"), true, 1). st_hpd(sit("a homeless man"), true, 2). st_hpd(put_down("wait staff", "full meal", t), true, 3). st_hpd(pay("a homeless man", b), false).
```

---

## Story #42 — Partial Match (Similarity: 0.2273)

**Story:** 

### Predicted
```clingo
restaurant("fancy restaurant"). customer(c_group). member("David", c_group). member("Sarah", c_group). food("duck confit"). beverage("wine"). waiter("the waiter"). st_hpd(enter(c_group, "fancy restaurant"), true, 0). st_hpd(order_for("David", c_group, "duck confit", "the waiter"), true, 1). st_hpd(put_down("the waiter", "duck confit", t), true, 2). st_hpd(put_down("the waiter", "wine", t), true, 2). st_hpd(drink(c_group, "wine"), true, 2). st_hpd(eat(c_group, "duck confit"), true, 3).
```

### Ground Truth
```clingo
restaurant("fancy restaurant"). customer(they). person("David"). person("Sarah"). member("David", they). member("Sarah", they). food("duck confit"). beverage("wine"). waiter("the waiter"). story_step(0..3). st_hpd(order_for("David", they, "duck confit", "the waiter"), true, 0). st_hpd(put_down("the waiter", "duck confit", t), true, 1). st_hpd(put_down("the waiter", "wine", t), true, 2). st_hpd(eat(they, "duck confit"), true, 3). st_hpd(drink(they, "wine"), true, 3).
```

---

## Story #40 — Partial Match (Similarity: 0.2353)

**Story:** 

### Predicted
```clingo
restaurant("sushi restaurant"). customer("Ken"). food("tuna roll"). food("hair-free roll"). waiter("the waiter"). st_obs(in("Ken", "sushi restaurant"), true, 0). st_hpd(order("Ken", "tuna roll", "the waiter"), true, 1). st_hpd(put_down("the waiter", "tuna roll", t), true, 2). st_hpd(complain("Ken", "the waiter"), true, 3). st_next(2, 3). st_hpd(put_down("the waiter", "hair-free roll", t), true, 4).
```

### Ground Truth
```clingo
restaurant("sushi restaurant"). customer("Ken"). food("tuna roll"). food("new tuna roll"). waiter("the waiter"). story_step(0..4). st_hpd(order("Ken", "tuna roll", "the waiter"), true, 0). st_hpd(put_down("the waiter", "tuna roll", t), true, 1). st_hpd(complain("Ken", "the waiter"), true, 2). st_next(1, 2). st_hpd(put_down(w, "new tuna roll", t), true, 3).
```

---

## Story #18 — Partial Match (Similarity: 0.2381)

**Story:** 

### Predicted
```clingo
restaurant("meat restaurant"). customer("Herbie"). customer("his father"). food("steak"). food("haddock and creamed spinach"). food("lamb chops"). waiter("the waiter"). st_obs(in("Herbie", "meat restaurant"), true, 0). st_obs(in("his father", "meat restaurant"), true, 0). st_hpd(put_down("the waiter", "steak", t), true, 1). st_hpd(put_down("the waiter", "haddock and creamed spinach", t), true, 1). st_hpd(request("his father", "take the fish away", "the waiter"), true, 2). st_hpd(request("his father", "lamb chops", "the waiter"), true, 2). 
```

### Ground Truth
```clingo
restaurant("a meat restaurant"). customer("Herbie"). customer("his father"). food("a sizzling steak"). food("haddock and creamed spinach"). food("lamb chops"). waiter("the waiter"). story_step(0..4). st_obs(in("Herbie", "a meat restaurant"), true, 0). st_obs(in("his father", "a meat restaurant"), true, 0). st_hpd(put_down("the waiter", "a sizzling steak", t), true, 1). st_hpd(put_down("the waiter", "haddock and creamed spinach", t), true, 2). st_hpd(request("his father", pick_up("the waiter", "haddock and creamed spinach", t), "the waiter"), true, 3). st_hpd(order_for("his father", "Herbie", "lamb chops", "the waiter"), true, 4).
```

---

## Story #10 — Partial Match (Similarity: 0.2500)

**Story:** 

### Predicted
```clingo
restaurant(r). customer("Jim"). food("an appetizer"). waiter(w). st_obs(sitting("Jim"), true, 0). st_hpd(order("Jim", "an appetizer", w), true, 1). st_obs(served("Jim"), false, 2). st_hpd(leave("Jim"), true, 3).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer("Jim"). food("appetizer"). story_step(0..3). st_obs(sitting("Jim"), true, 0). st_hpd(order("Jim", "appetizer", w), true, 1). st_obs(served("Pete"), false, 2). st_hpd(leave("Jim"), true, 3).
```

---

## Story #88 — Partial Match (Similarity: 0.2500)

**Story:** 

### Predicted
```clingo
restaurant("little deli"). customer("I"). food("a turkey sandwich"). waiter(w). st_obs(hungry("I"), true, 0). st_hpd(enter("I", "little deli"), true, 1). st_hpd(order("I", "a turkey sandwich", w), true, 2). st_hpd(eat("I", "a turkey sandwich"), true, 3). st_obs(hungry("I"), false, 4).
```

### Ground Truth
```clingo
restaurant("little deli"). customer("I"). food("turkey sandwich"). st_obs(hungry("I"), true, 0). st_hpd(order("I", "turkey sandwich", w), true, 1). st_hpd(eat("I", "turkey sandwich"), true, 2).
```

---

## Story #94 — Partial Match (Similarity: 0.2500)

**Story:** 

### Predicted
```clingo
restaurant("new sushi place"). customer(c_group). food(f). st_hpd(enter(c_group, "new sushi place"), true, 0). st_hpd(eat(c_group, f), true, 1).
```

### Ground Truth
```clingo
restaurant("new sushi place"). customer("The couple"). food(f). st_hpd(enter("The couple", "new sushi place"), true, 0). st_hpd(eat("The couple", f), true, 1).
```

---

## Story #23 — Partial Match (Similarity: 0.2609)

**Story:** 

### Predicted
```clingo
restaurant(r). customer("I"). food("salmon"). beverage("red wine"). food("hors d'oeuvres"). waiter("the waiter"). waiter("our server"). st_hpd(read_menu("I"), true, 0). st_hpd(order("I", "salmon", w), true, 1). st_hpd(put_down("the waiter", "red wine", t), true, 2). st_hpd(drink("I", "red wine"), true, 3). st_hpd(put_down("our server", "hors d'oeuvres", t), true, 4). st_hpd(eat("I", "hors d'oeuvres"), true, 5). st_hpd(put_down("the waiter", "salmon", t), true, 6). st_hpd(eat("I", "salmon"), true, 7).
```

### Ground Truth
```clingo
restaurant(r). customer("I"). food(salmon). drink("red wine"). food("hors d'oeuvres"). waiter("the waiter"). story_step(0..7). st_hpd(pick_up("I", m, t), true, 0). st_hpd(order("I", salmon, "the waiter"), true, 1). st_hpd(put_down("I", "red wine", t), true, 2). st_hpd(drink("I", "red wine"), true, 3). st_hpd(put_down("the waiter", "hors d'oeuvres", t), true, 4). st_hpd(eat("I", "hors d'oeuvres"), true, 5). st_hpd(put_down("the waiter", salmon, t), true, 6). st_hpd(eat("I", salmon), true, 7).
```

---

## Story #66 — Partial Match (Similarity: 0.2632)

**Story:** 

### Predicted
```clingo
restaurant(r). customer("Charlie"). food("a burger"). waiter("the waiter"). st_hpd(enter("Charlie", r), true, 0). st_hpd(lead_to(w, "Charlie", t), true, 1). st_hpd(order("Charlie", "a burger", "the waiter"), true, 2). st_hpd(put_down("the waiter", "a burger", t), true, 3). st_hpd(eat("Charlie", "a burger"), true, 4). st_hpd(request("Charlie", b, "the waiter"), true, 5). st_hpd(pay("Charlie", b), true, 6). st_hpd(leave("Charlie"), true, 7).
```

### Ground Truth
```clingo
restaurant("a restaurant"). customer("Charlie"). food("burger"). waiter("the waiter"). story_step(0..7). st_hpd(enter("Charlie", "a restaurant"), true, 0). st_hpd(lead_to("the waiter", "Charlie", t), true, 1). st_hpd(order("Charlie", "burger", "the waiter"), true, 2). st_hpd(put_down("the waiter", "burger", t), true, 3). st_hpd(eat("Charlie", "burger"), true, 4). st_hpd(request("Charlie", b, "the waiter"), true, 5). st_hpd(pay("Charlie", b), true, 6). st_hpd(leave("Charlie"), true, 7).
```

---

## Story #65 — Partial Match (Similarity: 0.2692)

**Story:** 

### Predicted
```clingo
restaurant("Italian restaurant"). customer("Maria"). host("the host"). food("spaghetti carbonara"). beverage("a glass of red wine"). waiter("the waiter"). st_hpd(enter("Maria", "Italian restaurant"), true, 0). st_hpd(greet("the host", "Maria"), true, 1). st_hpd(lead_to("the host", "Maria", t), true, 2). st_hpd(read_menu("Maria"), true, 3). st_hpd(order("Maria", "spaghetti carbonara", "the waiter"), true, 4). st_hpd(order("Maria", "a glass of red wine", "the waiter"), true, 4). st_hpd(put_down("the waiter", "spaghetti carbonara", t), true, 5). st_hpd(put_down("the waiter", "a glass of red wine", t), true, 5). st_hpd(eat("Maria", "spaghetti carbonara"), true, 6). st_hpd(drink("Maria", "a glass of red wine"), true, 6). st_hpd(request("Maria", b, "the waiter"), true, 7).
```

### Ground Truth
```clingo
restaurant("Italian restaurant"). customer("Maria"). person("the host"). food("spaghetti carbonara"). beverage("red wine"). waiter("the waiter"). story_step(0..6). st_hpd(enter("Maria", "Italian restaurant"), true, 0). st_hpd(greet("the host", "Maria"), true, 1). st_hpd(lead_to("the host", "Maria", t), true, 2). st_hpd(order("Maria", "spaghetti carbonara", "the waiter"), true, 3). st_hpd(order("Maria", "red wine", "the waiter"), true, 3). st_hpd(put_down("the waiter", "spaghetti carbonara", t), true, 4). st_hpd(put_down("the waiter", "red wine", t), true, 4). st_hpd(eat("Maria", "spaghetti carbonara"), true, 5). st_hpd(drink("Maria", "red wine"), true, 5). st_hpd(request("Maria", b, "the waiter"), true, 6).
```

---

## Story #7 — Partial Match (Similarity: 0.2727)

**Story:** 

### Predicted
```clingo
restaurant(r). customer("Larry"). waiter("the waiter"). st_obs(sitting("Larry"), true, 0). st_hpd(put_down("the waiter", menu, t), true, 1). st_hpd(read_menu("Larry"), true, 2). st_hpd(order("Larry"), false).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer("Larry"). waiter("the waiter"). story_step(0..3). st_obs(sitting("Larry"), true, 0). st_hpd(put_down("the waiter", m, t), true, 1). st_obs(menu_read("Larry"), true, 2). st_hpd(order("Larry"), false, 3).
```

---

## Story #58 — Partial Match (Similarity: 0.2778)

**Story:** 

### Predicted
```clingo
restaurant("the diner"). customer("Ben"). food(f). member("pancakes", f). member("bacon", f). beverage("coffee"). person("the cook"). waiter(w). st_hpd(enter("Ben", "the diner"), true, 0). st_hpd(sit("Ben"), true, 1). st_hpd(order("Ben", f, w), true, 2). st_hpd(order("Ben", "coffee", w), true, 2). st_hpd(prepare("the cook", f, w), true, 3). st_hpd(prepare("the cook", "coffee", w), true, 3).
```

### Ground Truth
```clingo
restaurant("the diner"). customer("Ben"). food("pancakes with bacon"). beverage("coffee"). story_step(0..3). st_hpd(enter("Ben", "the diner"), true, 0). st_hpd(sit("Ben"), true, 1). st_hpd(order("Ben", "pancakes with bacon", w), true, 2). st_hpd(prepare("the cook", "pancakes with bacon", w), true, 3). st_hpd(prepare("the cook", "coffee", "Ben"), true, 3).
```

---

## Story #93 — Partial Match (Similarity: 0.2778)

**Story:** 

### Predicted
```clingo
restaurant("the restaurant"). restaurant("Burger King"). customer(c_group). member("I", c_group). member("my mother", c_group). food("steak"). waiter(w). st_hpd(sit(c_group), true, 0). st_hpd(order("I", "steak", w), true, 1). st_obs(available("steak", "the restaurant"), false, 1). st_hpd(leave(c_group), true, 2). st_hpd(enter(c_group, "Burger King"), true, 3).
```

### Ground Truth
```clingo
restaurant("the restaurant"). restaurant("Burger King"). customer(we). person("I"). person("my mother"). food("steak"). st_hpd(sit(we), true, 0). st_hpd(order("I", "steak", w), true, 1). st_obs(available("steak", "the restaurant"), false, 1). st_hpd(leave(we), true, 2). st_hpd(enter(we, "Burger King"), true, 3).
```

---

## Story #85 — Partial Match (Similarity: 0.2857)

**Story:** 

### Predicted
```clingo
restaurant(r). customer("I"). food("a pizza"). food("burnt pizza"). waiter(w). st_hpd(enter("I", r), true, 0). st_hpd(order("I", "a pizza", w), true, 1). st_hpd(put_down(w, "burnt pizza", t), true, 2). st_hpd(request("I", "return it", w), true, 3). st_hpd(leave("I"), true, 4).
```

### Ground Truth
```clingo
restaurant("a restaurant"). customer("I"). food("pizza"). food("burnt pizza"). st_hpd(enter("I", r), true, 0). st_hpd(order("I", "pizza", w), true, 1). st_hpd(put_down(w, "burnt pizza", t), true, 2). st_hpd(request("I", pick_up(w, "burnt pizza", t), w), true, 3).
```

---

## Story #92 — Partial Match (Similarity: 0.3077)

**Story:** 

### Predicted
```clingo
restaurant("new restaurant"). customer("I"). food("a large salad"). waiter(w). st_obs(in("I", "new restaurant"), true, 0). st_hpd(order("I", "a large salad", w), true, 1). st_hpd(put_down(w, "a large salad", t), true, 2). st_hpd(complain("I", w), true, 3). st_next(2, 3).
```

### Ground Truth
```clingo
restaurant("new restaurant"). customer("I"). food("large salad"). food("small salad"). waiter(w). st_obs(in("I", "new restaurant"), true, 0). st_hpd(order("I", "large salad", w), true, 1). st_hpd(put_down(w, "small salad", t), true, 2).
```

---

## Story #20 — Partial Match (Similarity: 0.3182)

**Story:** 

### Predicted
```clingo
restaurant(r). customer(c_group). member("Molly", c_group). member("me", c_group). food("escargot"). food(f). member("twelve oysters", f). member("twelve clams", f). beverage("wine"). waiter("the waiter"). st_hpd(put_down("the waiter", "escargot", t), true, 0). st_hpd(put_down("the waiter", f, t), true, 1). st_hpd(eat(c_group, f), true, 2). st_hpd(put_down("the waiter", "wine", t), true, 3). st_hpd(drink(c_group, "wine"), true, 3).
```

### Ground Truth
```clingo
restaurant(r). customer(we). member("Molly", we). member(me, we). food(escargot). food(f). member("twelve oysters", f). member("twelve clams", f). beverage("wine"). waiter("the waiter"). story_step(0..3). st_hpd(put_down("the waiter", escargot, t), true, 0). st_hpd(put_down("the waiter", f, t), true, 1). st_hpd(eat(we, f), true, 2). st_hpd(put_down("the waiter", wine, t), true, 3).
```

---

## Story #4 — Partial Match (Similarity: 0.3333)

**Story:** 

### Predicted
```clingo
restaurant(r). customer("Bob"). food("a hamburger"). waiter("the waiter"). st_obs(sitting("Bob"), true, 0). st_hpd(order("Bob", "a hamburger", "the waiter"), true, 1).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer("Bob"). food("hamburger"). waiter("the waiter"). story_step(0..1). st_obs(sitting("Bob"), true, 0). st_hpd(order("Bob", "hamburger", "the waiter"), true, 1).
```

---

## Story #43 — Partial Match (Similarity: 0.3333)

**Story:** 

### Predicted
```clingo
restaurant(r). customer("Megan"). beverage("a glass of wine"). waiter("the bartender"). st_hpd(enter("Megan", r), true, 0). st_hpd(sit("Megan"), true, 1). st_hpd(order("Megan", "a glass of wine", "the bartender"), true, 2). st_hpd(drink("Megan", "a glass of wine"), true, 3). st_hpd(pay("Megan", b), true, 4). st_hpd(leave("Megan"), true, 5).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer("Megan"). beverage("glass of wine"). waiter("the bartender"). st_hpd(enter("Megan", "the restaurant"), true, 0). st_hpd(sit("Megan"), true, 1). st_hpd(order("Megan", "glass of wine", "the bartender"), true, 2). st_hpd(drink("Megan", "glass of wine"), true, 3). st_hpd(pay("Megan", b), true, 4). st_hpd(leave("Megan"), true, 5).
```

---

## Story #55 — Partial Match (Similarity: 0.3333)

**Story:** 

### Predicted
```clingo
restaurant("sushi restaurant"). customer("Mark"). customer("Lisa"). food("tuna rolls"). food("salmon nigiri"). person("the chef"). st_hpd(enter("Mark", "sushi restaurant"), true, 0). st_hpd(enter("Lisa", "sushi restaurant"), true, 0). st_hpd(sit("Mark"), true, 1). st_hpd(sit("Lisa"), true, 1). st_hpd(order("Mark", "tuna rolls", w), true, 2). st_hpd(order("Lisa", "salmon nigiri", w), true, 2). st_hpd(prepare("the chef", "tuna rolls", w), true, 3). st_hpd(prepare("the chef", "salmon nigiri", w), true, 3).
```

### Ground Truth
```clingo
restaurant("sushi restaurant"). waiter(w). person("Mark"). person("Lisa"). customer("they"). member("Mark", "they"). member("Mark", "they"). food("tuna rolls"). food("salmon nigiri"). story_step(0..4). st_hpd(enter("they", "sushi restaurant"), true, 0). st_obs(sitting("they"), true, 1). st_hpd(order("Mark", "tuna rolls", w), true, 2). st_hpd(order("Lisa", "salmon nigiri", w), true, 2). st_hpd(prepare("the chef", "tuna rolls", w), true, 3). st_hpd(prepare("the chef", "salmon nigiri", w), true, 3).
```

---

## Story #56 — Partial Match (Similarity: 0.3333)

**Story:** 

### Predicted
```clingo
restaurant("vegan restaurant"). customer("Anna"). food("quinoa bowl"). beverage("a green smoothie"). waiter(w). st_hpd(enter("Anna", "vegan restaurant"), true, 0). st_hpd(order("Anna", "quinoa bowl", w), true, 1). st_hpd(order("Anna", "a green smoothie", w), true, 1). st_hpd(eat("Anna", "quinoa bowl"), true, 2). st_hpd(drink("Anna", "a green smoothie"), true, 2). st_hpd(pay("Anna", tip), true, 3).
```

### Ground Truth
```clingo
restaurant("vegan restaurant"). customer("Anna"). food("quinoa bowl"). beverage("green smoothie"). waiter(w). story_step(0..4). st_hpd(enter("Anna", "vegan restaurant"), true, 0). st_hpd(order("Anna", "quinoa bowl", w), true, 1). st_hpd(order("Anna", "green smoothie", w), true, 1). st_hpd(put_down("the waiter", "quinoa bowl", t), true, 2). st_hpd(put_down("the waiter", "green smoothie", t), true, 2). st_hpd(eat("Anna", "quinoa bowl"), true, 3). st_hpd(drink("Anna", "green smoothie"), true, 3). st_hpd(pay("Anna", tip), true, 4).
```

---

## Story #44 — Partial Match (Similarity: 0.3571)

**Story:** 

### Predicted
```clingo
restaurant("Italian restaurant"). customer("Chloe"). food("lasagna"). food("spaghetti"). waiter("the waiter"). st_obs(in("Chloe", "Italian restaurant"), true, 0). st_hpd(order("Chloe", "lasagna", "the waiter"), true, 1). st_hpd(put_down("the waiter", "spaghetti", t), true, 2). st_hpd(complain("Chloe", "the waiter"), true, 3). st_next(2, 3).
```

### Ground Truth
```clingo
restaurant("Italian restaurant"). customer("Chloe"). food("lasagna"). food("spaghetti"). waiter("the waiter"). story_step(0..2). st_hpd(order("Chloe", "lasagna", "the waiter"), true, 0). st_hpd(put_down("the waiter", "spaghetti", t), true, 1). st_hpd(complain("Chloe", "the waiter"), true, 2). st_next(1, 2).
```

---

## Story #49 — Partial Match (Similarity: 0.3636)

**Story:** 

### Predicted
```clingo
restaurant(r). customer("Mark"). food("a dessert"). waiter("the waiter"). st_hpd(order("Mark", "a dessert", "the waiter"), false). st_hpd(put_down("the waiter", b, t), true, 0). st_hpd(read_bill("Mark"), true, 1). st_hpd(request("Mark", "correct the bill", "the waiter"), true, 2).
```

### Ground Truth
```clingo
restaurant(r). customer("Mark"). food("dessert"). waiter("the waiter"). st_hpd(put_down("the waiter", b, t), true, 0). st_hpd(pick_up("Mark", b, t), true, 1). st_hpd(request("Mark", "correction", "the waiter"), true, 1).
```

---

## Story #78 — Partial Match (Similarity: 0.3684)

**Story:** 

### Predicted
```clingo
restaurant("a diner"). customer("Betsy"). food(f). member("pancakes", f). member("bacon", f). beverage("coffee"). waiter("the waitress"). st_obs(hungry("Betsy"), true, 0). st_hpd(enter("Betsy","a diner"), true, 1). st_hpd(order("Betsy", f, "the waitress"), true, 2). st_hpd(order("Betsy", "coffee", "the waitress"), true, 2). st_hpd(eat("Betsy", f), true, 3). st_hpd(drink("Betsy", "coffee"), true, 3). st_hpd(pay("Betsy", tip), true, 4).
```

### Ground Truth
```clingo
restaurant("a diner"). customer("Betsy"). food(f). member("pancakes", f). member("bacon", f). beverage("coffee"). waiter("the waitress"). st_hpd(order("Betsy", f, "the waitress"), true, 0). st_hpd(order("Betsy", "coffee", "the waitress"), true, 0). st_hpd(eat("Betsy", f), true, 1). st_hpd(drink("Betsy", "coffee"), true, 1). st_hpd(pay("Betsy", tip), true, 2).
```

---

## Story #62 — Partial Match (Similarity: 0.3846)

**Story:** 

### Predicted
```clingo
restaurant("the steakhouse"). customer("Wendy"). food("rare steak"). food("well-done"). waiter("the waiter"). st_hpd(order("Wendy", "well-done", "the waiter"), true, 0). st_hpd(put_down("the waiter", "rare steak", t), true, 1). st_next(0, 1). st_hpd(request("Wendy", "return the steak", "the waiter"), true, 2).
```

### Ground Truth
```clingo
restaurant("the steakhouse"). customer("Wendy"). food("rare steak"). food("well-done steak"). waiter("the waiter"). story_step(0..2). st_hpd(order("Wendy", "well-done steak", "the waiter"), true, 0). st_hpd(put_down("the waiter", "rare steak", t), true, 1). st_hpd(request("Wendy", pick_up("the waiter", "rare steak", t), "the waiter"), true, 2). st_next(1, 2).
```

---

## Story #97 — Partial Match (Similarity: 0.3846)

**Story:** 

### Predicted
```clingo
restaurant(r). customer("Tim"). food(f). waiter("the waiter"). st_obs(in("Tim", r), true, 0). st_hpd(put_down("the waiter", f, t), true, 1). st_hpd(order("Tim", f, "the waiter"), false). st_hpd(complain("Tim", "the waiter"), true, 2). st_next(1, 2).
```

### Ground Truth
```clingo
restaurant(r). customer("Tim"). food("wrong order"). waiter("the waiter"). st_obs(in("Tim", r), true, 0). st_hpd(put_down("the waiter", "wrong order", t), true, 1). st_hpd(complain("Tim", "the waiter"), true, 2). st_next(1, 2). st_hpd(put_down("the waiter", f, t), true, 3).
```

---

## Story #17 — Partial Match (Similarity: 0.4000)

**Story:** 

### Predicted
```clingo
restaurant(r). customer("He"). food("something spotted with eggs and livers"). waiter("the waiter"). st_hpd(put_down("the waiter", "something spotted with eggs and livers", t), true, 0). st_hpd(eat("He", "something spotted with eggs and livers"), true, 1). st_hpd(request("He", b, "the waiter"), true, 2). st_hpd(put_down("the waiter", b, t), false).
```

### Ground Truth
```clingo
customer("he"). food("something spotted with eggs and livers"). waiter("the waiter"). story_step(0..1). st_hpd(put_down("the waiter", "something spotted with eggs and livers", t), true, 0). st_hpd(eat("he", "something spotted with eggs and livers"), true, 1). st_hpd(put_down("the waiter", b, t), false).
```

---

## Story #60 — Partial Match (Similarity: 0.4000)

**Story:** 

### Predicted
```clingo
restaurant(r). customer("Robert"). food("medium-rare steak"). food("well-done one"). waiter("the waiter"). st_hpd(order("Robert", "medium-rare steak", "the waiter"), true, 0). st_hpd(put_down("the waiter", "well-done one", t), true, 1). st_hpd(complain("Robert", "the waiter"), true, 2). st_next(1, 2). st_hpd(pick_up("the waiter", "well-done one", t), true, 3). st_hpd(move("the waiter", t, "kitchen"), true, 4).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer("Robert"). food("medium-rare steak"). food("well-done steak"). waiter("the waiter"). story_step(0..3). st_hpd(order("Robert", "medium-rare steak", "the waiter"), true, 0). st_hpd(put_down("the waiter", "well-done steak", t), true, 1). st_hpd(complain("Robert", "the waiter"), true, 2). st_next(1, 2). st_hpd(pick_up("the waiter", "well-done steak", t), true, 3).
```

---

## Story #91 — Partial Match (Similarity: 0.4000)

**Story:** 

### Predicted
```clingo
restaurant("fast food restaurant"). customer("Emily"). food("fries"). food("a burger"). waiter("the cashier"). st_hpd(order("Emily", "fries", "the cashier"), true, 0). st_hpd(order("Emily", "a burger", "the cashier"), true, 0). st_hpd(put_down("the cashier", "a burger", t), true, 1). st_hpd(put_down("the cashier", "fries", t), false). st_hpd(complain("Emily", "the cashier"), true, 2).
```

### Ground Truth
```clingo
restaurant("fast food restaurant"). customer("Emily"). food("fries"). food("burger"). waiter("the cashier"). st_hpd(order("Emily", "fries", "the cashier"), true, 0). st_hpd(order("Emily", "burger", "the cashier"), true, 0). st_hpd(put_down("the cashier", "burger", t), true, 1). st_hpd(put_down("the cashier", "fries", t), false). st_hpd(complain("Emily", "the cashier"), true, 2). st_next(1,2).
```

---

## Story #73 — Partial Match (Similarity: 0.4118)

**Story:** 

### Predicted
```clingo
restaurant("deli"). customer("David"). food(f). member("a pastrami sandwich", f). member("a pickle",f). person("the cook"). waiter("the server"). st_hpd(enter("David", "deli"), true, 0). st_hpd(sit("David"), true, 1). st_hpd(order("David", f, "the server"), true, 2). st_hpd(prepare("the cook", f, "the server"), true, 3). st_hpd(put_down("the server", f, t), true, 4). st_hpd(eat("David", f), true, 5).
```

### Ground Truth
```clingo
restaurant("the deli"). customer("David"). food(f). member("pastrami sandwich", f). member("pickle", f). st_hpd(enter("David", "the deli"), true, 0). st_hpd(sit("David"), true, 1). st_hpd(order("David", f, "the server"), true, 2). st_hpd(prepare("the cook", f, "the server"), true, 3). st_hpd(put_down("the server", f, t), true, 4). st_hpd(eat("David", f), true, 5).
```

---

## Story #84 — Partial Match (Similarity: 0.4167)

**Story:** 

### Predicted
```clingo
restaurant("the diner"). customer("Donna"). food(f). member("the cheeseburger", f). member("onion rings", f). waiter(w). st_hpd(enter("Donna", "the diner"), true, 0). st_hpd(order("Donna", f, w), true, 1). st_hpd(eat("Donna", f), true, 2).
```

### Ground Truth
```clingo
restaurant("diner"). customer("Donna"). food(f). member("cheeseburger", f). member("onion rings", f). st_hpd(enter("Donna", "diner"), true, 0). st_hpd(order("Donna", f, w), true, 1). st_hpd(eat("Donna", f), true, 2).
```

---

## Story #48 — Partial Match (Similarity: 0.4545)

**Story:** 

### Predicted
```clingo
restaurant(r). customer("Olivia"). beverage("a glass of water"). waiter("the waiter"). st_hpd(sit("Olivia"), true, 0). st_hpd(greet("the waiter", "Olivia"), true, 1). st_hpd(order("Olivia", "a glass of water", "the waiter"), true, 1). st_hpd(put_down("the waiter", "a glass of water", t), true, 2).
```

### Ground Truth
```clingo
restaurant(r). customer("Olivia"). beverage("glass of water"). waiter("the waiter"). story_step(0..3). st_hpd(sit("Olivia"), true, 0). st_hpd(greet("the waiter", "Olivia"), true, 1). st_hpd(order("Olivia", "glass of water", "the waiter"), true, 2). st_hpd(put_down("the waiter", "glass of water", t), true, 3).
```

---

## Story #9 — Partial Match (Similarity: 0.4667)

**Story:** 

### Predicted
```clingo
restaurant(r). customer("Pete"). food("chicken"). waiter("the waiter"). st_obs(sitting("Pete"), true, 0). st_hpd(order("Pete", "chicken", "the waiter"), true, 1). st_hpd(put_down("the waiter", "chicken", t), true, 2). st_hpd(complain("Pete", "the waiter"), true, 3). st_next(2, 3). st_hpd(request("Pete", "a better cooked dish", "the waiter"), true, 3).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer("Pete"). food("chicken"). food("undercooked chicken"). food("better cooked chicken"). waiter("the waiter"). story_step(0..4). st_obs(sitting("Pete"), true, 0). st_hpd(order("Pete", "chicken", "the waiter"), true, 1). st_hpd(put_down("the waiter", "undercooked_chicken", t), true, 2). st_hpd(complain("Pete", "the waiter"), true, 3). st_next(2, 3). st_hpd(order("Pete", "better cooked chicken", "the waiter"), true, 4).
```

---

## Story #57 — Partial Match (Similarity: 0.5294)

**Story:** 

### Predicted
```clingo
restaurant("Mexican restaurant"). customer("Carlos"). food("tacos"). beverage("a margarita"). waiter(w). st_hpd(enter("Carlos", "Mexican restaurant"), true, 0). st_hpd(greet(w, "Carlos"), true, 1). st_hpd(order("Carlos", "tacos", w), true, 2). st_hpd(order("Carlos", "a margarita", w), true, 2). st_hpd(put_down(w, "tacos", t), true, 3). st_hpd(put_down(w, "a margarita", t), true, 3). st_hpd(eat("Carlos", "tacos"), true, 4). st_hpd(drink("Carlos", "a margarita"), true, 4).
```

### Ground Truth
```clingo
restaurant("Mexican restaurant"). customer("Carlos"). waiter(w). food("tacos"). beverage("margarita"). story_step(0..4). st_hpd(enter("Carlos", "Mexican restaurant"), true, 0). st_hpd(greet(w, "Carlos"), true, 1). st_hpd(order("Carlos", "tacos", w), true, 2). st_hpd(order("Carlos", "margarita", w), true, 2). st_hpd(put_down(w, "tacos", t), true, 3). st_hpd(put_down(w, "margarita", t), true, 3). st_hpd(eat("Carlos", "tacos"), true, 4). st_hpd(drink("Carlos", "margarita"), true, 4).
```

---

## Story #41 — Partial Match (Similarity: 0.5714)

**Story:** 

### Predicted
```clingo
restaurant("cafe"). customer("Laura"). beverage("coffee"). food("croissant"). waiter("the waiter"). st_hpd(order("Laura", "coffee", "the waiter"), true, 0). st_hpd(order("Laura", "croissant", "the waiter"), true, 0). st_hpd(put_down("the waiter", "coffee", t), true, 1). st_hpd(put_down("the waiter", "croissant", t), false). st_hpd(pay("Laura", b), true, 2). st_hpd(leave("Laura"), true, 3).
```

### Ground Truth
```clingo
restaurant("cafe"). customer("Laura"). beverage("coffee"). food("croissant").  waiter("the waiter"). story_step(0..4). st_hpd(order("Laura", "coffee", "the waiter"), true, 0). st_hpd(order("Laura", "croissant", "the waiter"), true, 0). st_hpd(put_down("the waiter", "coffee", t), true, 1). st_obs(served("Laura"), false, 2). st_hpd(pay("Laura", b), true, 3). st_hpd(leave("Laura"), true, 4).
```

---

## Story #59 — Partial Match (Similarity: 0.5833)

**Story:** 

### Predicted
```clingo
restaurant("health food restaurant"). customer("Lucy"). food("kale salad"). beverage("detox juice"). waiter(w). st_hpd(enter("Lucy", "health food restaurant"), true, 0). st_hpd(order("Lucy", "kale salad", w), true, 1). st_hpd(order("Lucy", "detox juice", w), true, 1). st_hpd(eat("Lucy", "kale salad"), true, 2). st_hpd(drink("Lucy", "detox juice"), true, 2).
```

### Ground Truth
```clingo
restaurant("health food restaurant"). customer("Lucy"). food("kale salad"). beverage("detox juice"). story_step(0..2). st_hpd(enter("Lucy", "health food restaurant"), true, 0). st_hpd(order("Lucy", "kale salad", "the waiter"), true, 1). st_hpd(order("Lucy", "detox juice", "the waiter"), true, 1). st_hpd(eat("Lucy", "kale salad"), true, 2). st_hpd(drink("Lucy", "detox juice"), true, 2).
```

---

## Story #50 — Partial Match (Similarity: 0.6000)

**Story:** 

### Predicted
```clingo
restaurant(r). customer("Fiona"). food("soup of the day"). food("a sandwich"). waiter("the waiter"). st_hpd(order("Fiona", "soup of the day", "the waiter"), true, 0). st_obs(available("soup of the day", r), false, 1). st_hpd(order("Fiona", "a sandwich", "the waiter"), true, 2).
```

### Ground Truth
```clingo
restaurant(r). customer("Fiona"). food("soup of the day"). food("sandwich"). waiter("the waiter"). story_step(0..2). st_hpd(order("Fiona", "soup of the day", "the waiter"), true, 0). st_obs(available("soup of the day", r), false, 1). st_hpd(order("Fiona", "sandwich", "the waiter"), true, 2).
```

---

## Story #68 — Partial Match (Similarity: 0.6000)

**Story:** 

### Predicted
```clingo
restaurant("local diner"). customer("Frank"). beverage("a black coffee"). food("pancakes"). waiter("the waitress"). st_hpd(sit("Frank"), true, 0). st_hpd(put_down("the waitress", "a black coffee", t), true, 1). st_hpd(read_menu("Frank"), true, 2). st_hpd(order("Frank", "pancakes", "the waitress"), true, 3). st_hpd(eat("Frank", "pancakes"), true, 4). st_hpd(pay("Frank", b), true, 5). st_hpd(leave("Frank"), true, 6).
```

### Ground Truth
```clingo
restaurant("local diner"). customer("Frank"). beverage("black coffee"). food("pancakes"). waiter("the waitress"). story_step(0..6). st_obs(sitting("Frank"), true, 0). st_hpd(put_down("the waitress", "black coffee", t), true, 1). st_hpd(read_menu("Frank"), true, 2). st_hpd(order("Frank", "pancakes", "the waitress"), true, 3). st_hpd(eat("Frank", "pancakes"), true, 4). st_hpd(pay("Frank", b), true, 5). st_hpd(leave("Frank"), true, 6).
```

---

## Story #72 — Partial Match (Similarity: 0.6000)

**Story:** 

### Predicted
```clingo
restaurant("pancake house"). customer("Susan"). food("blueberry pancakes"). beverage("orange juice"). waiter("the server"). st_hpd(enter("Susan", "pancake house"), true, 0). st_hpd(order("Susan", "blueberry pancakes", "the server"), true, 1). st_hpd(order("Susan", "orange juice", "the server"), true, 1). st_hpd(put_down("the server", "blueberry pancakes", t), true, 2). st_hpd(put_down("the server", "orange juice", t), true, 2). st_hpd(eat("Susan", "blueberry pancakes"), true, 3). st_hpd(drink("Susan", "orange juice"), true, 3). st_hpd(pay("Susan", b), true, 4).
```

### Ground Truth
```clingo
restaurant("the pancake house"). customer("Susan"). food("blueberry pancakes"). beverage("orange juice"). waiter("the server"). st_hpd(enter("Susan", "the pancake house"), true, 0). st_hpd(order("Susan", "blueberry pancakes", "the server"), true, 1). st_hpd(order("Susan", "orange juice", "the server"), true, 1). st_hpd(put_down("the server", "blueberry pancakes", t), true, 2). st_hpd(eat("Susan", "blueberry pancakes"), true, 3). st_hpd(pay("Susan", b), true, 4).
```

---

## Story #8 — Partial Match (Similarity: 0.6364)

**Story:** 

### Predicted
```clingo
restaurant(r). customer("Derek"). food("vegetable soup"). waiter("the waiter"). st_hpd(order("Derek", "vegetable soup", "the waiter"), true, 0). st_hpd(put_down("the waiter", "vegetable soup", t), true, 1). st_hpd(complain("Derek", "the waiter"), true, 2). st_next(1, 2). st_hpd(cancel_bill("the waiter"), true, 3).
```

### Ground Truth
```clingo
restaurant("restaurant"). customer("Derek"). food("vegetable soup"). waiter("the waiter"). story_step(0..3). st_hpd(order("Derek", "vegetable soup", "the waiter"), true, 0). st_hpd(put_down("the waiter", "vegetable soup", t), true, 1). st_hpd(complain("Derek", "the waiter"), true, 2). st_next(1, 2). st_hpd(pay("derek", b), false, 3).
```

---

## Story #16 — Partial Match (Similarity: 0.6667)

**Story:** 

### Predicted
```clingo
restaurant(r). customer("Gavin"). customer("Amandine"). food(f). member("egg drop soup with wonton", f). member("lobster Cantonese and shrimp", f). member("beef and pork fried rice", f). waiter("the waiter"). st_hpd(lead_to("the waiter", "Gavin", t), true, 0). st_hpd(lead_to("the waiter", "Amandine", t), true, 0). st_hpd(sit("Gavin"), true, 1). st_hpd(sit("Amandine"), true, 1). st_hpd(read_menu("Gavin"), true, 2). st_hpd(order("Amandine", f, "the waiter"), true, 3). st_hpd(order("Gavin", f, "the waiter"), true, 4).
```

### Ground Truth
```clingo
waiter("the waiter"). customer("Gavin"). customer("Amandine"). food(f). member("egg drop soup with wonton", f). member("lobster Cantonese", f). member("shrimp, beef and pork fried rice", f). story_step(0..4). st_hpd(lead_to("the waiter", "Gavin", t), true, 0). st_hpd(lead_to("the waiter", "Amandine", t), true, 0). st_hpd(sit("Gavin"), true, 1). st_hpd(sit("Amandine"), true, 1). st_hpd(read_menu("Gavin"), true, 2). st_hpd(read_menu("Amandine"), false). st_hpd(order("Amandine", f, "the waiter"), true, 3). st_hpd(order("Gavin", f, "the waiter"), true, 4).
```

---

## Story #0 — Partial Match (Similarity: 0.6923)

**Story:** 

### Predicted
```clingo
restaurant(r). customer("Allie"). waiter("the waiter"). food("fruit salad"). st_hpd(enter("Allie", r), true, 0). st_hpd(lead_to("the waiter", "Allie", t), true, 1). st_hpd(sit("Allie"), true, 2). st_hpd(order("Allie", "fruit salad", "the waiter"), true, 3). st_hpd(put_down("the waiter", "fruit salad", t), true, 4). st_hpd(eat("Allie", "fruit salad"), true, 5). st_hpd(request("Allie", b, "the waiter"), true, 6).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer("Allie"). food("fruit salad"). waiter("the waiter"). story_step(0..6). st_hpd(enter("Allie", "the restaurant"), true, 0). st_hpd(lead_to("the waiter", "Allie", t), true, 1). st_hpd(sit("Allie"), true, 2). st_hpd(order("Allie", "fruit salad", "the waiter"), true, 3). st_hpd(put_down("the waiter", "fruit salad", t), true, 4). st_hpd(eat("Allie", "fruit salad"), true, 5). st_hpd(request("Allie", b, "the waiter"), true, 6).
```

---

## Story #6 — Partial Match (Similarity: 0.7778)

**Story:** 

### Predicted
```clingo
restaurant(r). customer("Molly"). food("baked potato"). food("French fries"). waiter("the waiter"). st_obs(sitting("Molly"), true, 0). st_hpd(order("Molly", "baked potato", "the waiter"), true, 1). st_hpd(put_down("the waiter", "French fries", t), true, 2).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer("Molly"). food("baked potato"). food("French fries"). waiter("the waiter"). story_step(0..2). st_obs(sitting("Molly"), true, 0). st_hpd(order("Molly", "baked potato", "the waiter"), true, 1). st_hpd(put_down("the waiter", "French fries", t), true, 2).
```

---

## Story #11 — Partial Match (Similarity: 0.7778)

**Story:** 

### Predicted
```clingo
restaurant(r). customer("Jake"). food("medium-rare steak"). food("too rare steak"). waiter("the waiter"). st_obs(sitting("Jake"), true, 0). st_hpd(order("Jake", "medium-rare steak", "the waiter"), true, 1). st_hpd(put_down("the waiter", "too rare steak", t), true, 2).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer("Jake"). food("medium-rare steak"). food("too rare steak"). waiter("the waiter"). story_step(0..2). st_obs(sitting("Jake"), true, 0). st_hpd(order("Jake", "medium-rare steak", "the waiter"), true, 1). st_hpd(put_down("the waiter", "too rare steak", t), true, 2).
```

---

## Story #5 — Partial Match (Similarity: 0.8000)

**Story:** 

### Predicted
```clingo
restaurant(r). customer("Jane"). food("fish"). waiter("the waiter"). st_hpd(lead_to("the waiter", "Jane", t), true, 0). st_obs(sitting("Jane"), true, 1). st_hpd(order("Jane", "fish", "the waiter"), true, 2). st_hpd(eat("Jane", "fish"), true, 3). st_hpd(put_down("the waiter", b, t), true, 4).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer("Jane"). food("fish"). waiter("the waiter"). story_step(0..4). st_hpd(lead_to("the waiter", "Jane", t), true, 0). st_obs(sitting("Jane"), true, 1). st_hpd(order("Jane", "fish", "the waiter"), true, 2). st_hpd(eat("Jane", "fish"), true, 3). st_hpd(put_down("the waiter", b, t), true, 4).
```

---

## Story #98 — Partial Match (Similarity: 0.8889)

**Story:** 

### Predicted
```clingo
restaurant("new place"). customer("Joe"). food("a meal"). waiter(w). st_obs(hungry("Joe"), true, 0). st_hpd(enter("Joe", "new place"), true, 1). st_hpd(order("Joe", "a meal", w), true, 2). st_hpd(eat("Joe", "a meal"), true, 3). st_obs(hungry("Joe"), false, 4).
```

### Ground Truth
```clingo
restaurant("new place"). customer("Joe"). food("a meal"). st_obs(hungry("Joe"), true, 0). st_hpd(enter("Joe", "new place"), true, 1). st_hpd(order("Joe", "a meal", w), true, 2). st_hpd(eat("Joe", "a meal"), true, 3). st_obs(hungry("Joe"), false, 4).
```

---

## Story #1 — Partial Match (Similarity: 1.0000)

**Story:** 

### Predicted
```clingo
restaurant("vegetarian restaurant"). customer("Abdul"). food("hummus"). waiter("the waiter"). st_obs(sitting("Abdul"), true, 0). st_hpd(order("Abdul", "hummus", "the waiter"), true, 1). st_hpd(put_down("the waiter", "hummus", t), true, 2).
```

### Ground Truth
```clingo
restaurant("vegetarian restaurant"). customer("Abdul"). food("hummus"). waiter("the waiter"). story_step(0..2). st_obs(sitting("Abdul"), true, 0). st_hpd(order("Abdul", "hummus", "the waiter"), true, 1). st_hpd(put_down("the waiter", "hummus", t), true, 2).
```

---

## Story #46 — Partial Match (Similarity: 1.0000)

**Story:** 

### Predicted
```clingo
restaurant(r). customer("Rita"). food("salad"). waiter("the waiter"). st_hpd(eat("Rita", "salad"), true, 0). st_hpd(request("Rita", b, "the waiter"), true, 1). st_hpd(put_down("the waiter", b, t), true, 2). st_hpd(pay("Rita", b), true, 3).
```

### Ground Truth
```clingo
restaurant(r). customer("Rita"). food("salad"). waiter("the waiter"). story_step(0..3). st_hpd(eat("Rita", "salad"), true, 0). st_hpd(request("Rita", b, "the waiter"), true, 1). st_hpd(put_down("the waiter", b, t), true, 2). st_hpd(pay("Rita", b), true, 3).
```

---

## Story #63 — Partial Match (Similarity: 1.0000)

**Story:** 

### Predicted
```clingo
restaurant("cafe"). customer("Ivan"). beverage("espresso"). waiter("the waiter"). st_hpd(order("Ivan", "espresso", "the waiter"), true, 0). st_hpd(put_down("the waiter", "espresso", t), true, 1). st_hpd(drink("Ivan", "espresso"), true, 2). st_hpd(pay("Ivan", b), true, 3). st_hpd(leave("Ivan"), true, 4).
```

### Ground Truth
```clingo
restaurant("cafe"). customer("Ivan"). beverage("espresso"). waiter("the waiter"). story_step(0..4). st_hpd(order("Ivan", "espresso", "the waiter"), true, 0). st_hpd(put_down("the waiter", "espresso", t), true, 1). st_hpd(drink("Ivan", "espresso"), true, 2). st_hpd(pay("Ivan", b), true, 3). st_hpd(leave("Ivan"), true, 4).
```

---
