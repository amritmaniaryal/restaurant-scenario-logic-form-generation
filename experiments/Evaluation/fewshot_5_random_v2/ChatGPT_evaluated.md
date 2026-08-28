# ChatGPT_evaluated

## Summary

- Total common: 100
- Exact matches: 5
- Partial matches: 95
- Accuracy: 0.05

---

## Story #26 — Partial Match (Similarity: 0.0000)

**Story:** 

### Predicted
```clingo
restaurant("vegetarian restaurant"). customer("Nicole"). food("lentil soup"). waiter("the waitress"). st_hpd(enter("Nicole", "vegetarian restaurant"), true, 0). st_hpd(order("Nicole", "lentil soup", "the waitress"), true, 1). st_hpd(put_down("the waitress", "lentil soup", t), true, 2). st_hpd(eat("Nicole", "lentil soup"), true, 3). st_hpd(leave("Nicole"), true, 4).
```

### Ground Truth
```clingo
restaurant(veg_r). customer(nicole). food(lentil_soup). waiter(waitress). story_step(0..4). st_hpd(enter(nicole, veg_r), true, 0). st_hpd(order(nicole, lentil_soup, waitress), true, 1). st_hpd(put_down(waitress, lentil_soup, t), true, 2). st_hpd(eat(nicole, lentil_soup), true, 3). st_hpd(leave(nicole), true, 4).
```

---

## Story #27 — Partial Match (Similarity: 0.0000)

**Story:** 

### Predicted
```clingo
restaurant("vegetarian restaurant"). customer("Nicole"). customer("Sam"). waiter("the waitress"). food("lentil soup"). food("miso soup"). st_hpd(enter("Nicole", "vegetarian restaurant"), true, 0). st_hpd(enter("Sam", "vegetarian restaurant"), true, 0). st_hpd(order("Nicole", "lentil soup", "the waitress"), true, 1). st_hpd(order("Sam", "miso soup", "the waitress"), true, 1). st_hpd(eat("Nicole", "lentil soup"), true, 2). st_hpd(eat("Sam", "miso soup"), true, 2).
```

### Ground Truth
```clingo
restaurant(veg_r). customer(nicole). customer(sam). food(lentil_soup). food(miso_soup). waiter(w). story_step(0..3). st_hpd(enter(nicole, veg_r), true, 0). st_hpd(enter(sam, veg_r), true, 0). st_hpd(order(nicole, lentil_soup, waitress), true, 1). st_hpd(order(sam, miso_soup, waitress), true, 2). st_hpd(eat(nicole, lentil_soup), true, 3). st_hpd(eat(sam, miso_soup), true, 3).
```

---

## Story #29 — Partial Match (Similarity: 0.0000)

**Story:** 

### Predicted
```clingo
restaurant("vegetarian restaurant"). customer("Nicole"). waiter("the waitress"). food("lentil soup"). st_hpd(enter("Nicole", "vegetarian restaurant"), true, 0). st_hpd(order("Nicole", "lentil soup", "the waitress"), true, 1). st_hpd(put_down("the waitress", "lentil soup", t), true, 2). st_hpd(cancel_bill("the waitress"), true, 3). st_hpd(eat("Nicole", "lentil soup"), true, 4). st_hpd(leave("Nicole"), true, 5).
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
restaurant("vegetarian restaurant"). customer("Nicole"). waiter("the waitress"). food("lentil soup"). food("miso soup"). st_hpd(enter("Nicole", "vegetarian restaurant"), true, 0). st_hpd(order("Nicole", "lentil soup", "the waitress"), true, 1). st_hpd(put_down("the waitress", "miso soup", t), true, 2).
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
restaurant("vegetarian restaurant"). customer("Nicole"). waiter("the waitress"). food("lentil soup"). food("miso soup"). st_hpd(enter("Nicole", "vegetarian restaurant"), true, 0). st_hpd(order("Nicole", "lentil soup", "the waitress"), true, 1). st_hpd(put_down("the waitress", "miso soup", t), true, 2). st_hpd(eat("Nicole", "miso soup"), true, 3).
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
restaurant("vegetarian restaurant"). customer("Nicole"). waiter("the waitress"). food("lentil soup"). st_hpd(enter("Nicole", "vegetarian restaurant"), true, 0). st_hpd(order("Nicole", "lentil soup", "the waitress"), true, 1). st_hpd(put_down("the waitress", "lentil soup", t), true, 2). st_hpd(pay("Nicole", b), true, 3). st_hpd(read_bill("Nicole"), false).
```

### Ground Truth
```clingo
restaurant(veg_r). customer(nicole). person(owner). food(lentil_soup). waiter(waitress). story_step(0..3). st_hpd(enter(nicole, veg_r), true, 0). st_hpd(order(nicole, lentil_soup, waitress), true, 1). st_hpd(put_down(waitress, miso_soup, t), true, 2). st_hpd(pay(nicole, b), true, 3). next_st(2, 3).
```

---

## Story #94 — Partial Match (Similarity: 0.0000)

**Story:** [REDACTED — original ROCStories text; storyid=63dfd3a4-930a-4a27-8ed9-60304b6c32f3]

### Predicted
```clingo
restaurant("new sushi place in town"). customer("the couple"). waiter("the waiter"). food("food"). st_hpd(enter("the couple", "new sushi place in town"), true, 0). st_hpd(order("the couple", "food", "the waiter"), true, 1). st_hpd(eat("the couple", "food"), true, 2).
```

### Ground Truth
```clingo
restaurant("new sushi place"). customer("The couple"). food(f). st_hpd(enter("The couple", "new sushi place"), true, 0). st_hpd(eat("The couple", f), true, 1).
```

---

## Story #95 — Partial Match (Similarity: 0.0000)

**Story:** [REDACTED — original ROCStories text; storyid=cd9a0a7b-ef8f-42c0-86ac-fe80542cebd3]

### Predicted
```clingo
restaurant("the restaurant"). customer("the homeless man"). waiter("the manager"). waiter("the wait staff"). st_hpd(lead_to("the manager", "the homeless man", t), true, 0). food("a full meal"). st_hpd(put_down("the wait staff", "a full meal", t), true, 1). st_hpd(cancel_bill("the wait staff"), true, 2).
```

### Ground Truth
```clingo
restaurant("a restaurant"). customer("a homeless man"). waiter("wait staff"). person("Austin"). food("spare food"). food("full meal").  st_hpd(enter("a homeless man", "a restaurant"), true, 0). st_hpd(request("a homeless man", "spare food", "Austin"), true, 1). st_hpd(sit("a homeless man"), true, 2). st_hpd(put_down("wait staff", "full meal", t), true, 3). st_hpd(pay("a homeless man", b), false).
```

---

## Story #99 — Partial Match (Similarity: 0.0000)

**Story:** [REDACTED — original ROCStories text; storyid=11cd400e-b2b8-4279-9e2e-925de49fee44]

### Predicted
```clingo
restaurant("new Mexican restaurant"). customer("the family"). waiter("the waiter"). food("chicken tacos"). st_hpd(enter("the family", "new Mexican restaurant"), true, 0). st_hpd(order("the family", "chicken tacos", "the waiter"), true, 1). st_hpd(eat("the family", "chicken tacos"), true, 2).
```

### Ground Truth
```clingo
restaurant("new restaurant"). customer("The family"). food("different foods"). food("tacos"). st_hpd(enter("The family", "new restaurant"), true, 0). st_hpd(order("The family", "different foods", w), true, 1). st_hpd(eat("The family", "different foods"), true, 2).
```

---

## Story #64 — Partial Match (Similarity: 0.0385)

**Story:** 

### Predicted
```clingo
restaurant("the restaurant"). customer("Penny"). customer("her friend"). waiter("the waiter"). st_hpd(enter("Penny", "the restaurant"), true, 0). st_hpd(enter("her friend", "the restaurant"), true, 0). st_hpd(lead_to("the waiter", "Penny", t), true, 1). st_hpd(lead_to("the waiter", "her friend", t), true, 1). st_hpd(read_menu("Penny"), true, 2). st_hpd(read_menu("her friend"), true, 2). food("their food"). st_hpd(order("Penny", "their food", "the waiter"), true, 3). st_hpd(order_for("Penny", "her friend", "their food", "the waiter"), true, 3). st_hpd(eat("Penny", "their food"), true, 4). st_hpd(eat("her friend", "their food"), true, 4).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer(they). person("Penny"). person("her friend"). member("Penny", they). member("her friend", they). food("food"). story_step(0..5). st_hpd(enter(they, "the restaurant"), true, 0). st_hpd(sit(they), true, 1). st_hpd(read_menu(they), true, 3). st_hpd(order(they, "food", w), true, 4). st_hpd(eat(they, "food"), true, 5).
```

---

## Story #82 — Partial Match (Similarity: 0.0417)

**Story:** [REDACTED — original ROCStories text; storyid=2cf524c3-5e49-4ba9-9590-f84429fbdc01]

### Predicted
```clingo
restaurant("the new restaurant"). customer("Elmer"). customer("Emma"). waiter("the waiter"). food(f). member("burgers", f). member("fries", f). beverage("milkshakes"). st_hpd(order("Elmer", f, "the waiter"), true, 0). st_hpd(order("Elmer", "milkshakes", "the waiter"), true, 0). st_hpd(order_for("Elmer", "Emma", f, "the waiter"), true, 0). st_hpd(order_for("Elmer", "Emma", "milkshakes", "the waiter"), true, 0).
```

### Ground Truth
```clingo
restaurant("new restaurant"). customer("the couple"). person("Elmer"). person("Emma"). member("Elmer", "the couple"). member("Emma", "the couple"). food("burgers"). food("fries"). beverage("milkshakes"). st_hpd(enter("the couple", "new restaurant"), true, 0). st_hpd(order("the couple", "burgers", w), true, 1). st_hpd(order("the couple", "milkshakes", w), true, 1). st_hpd(order("Elmer", "fries", w), true, 2).
```

---

## Story #13 — Partial Match (Similarity: 0.0435)

**Story:** 

### Predicted
```clingo
restaurant("local restaurant"). customer("Judy"). customer("Alex"). customer("Zoe"). waiter("the waiter"). st_obs(sitting("Judy"), true, 0). st_obs(sitting("Alex"), true, 0). st_obs(sitting("Zoe"), true, 0). st_hpd(read_menu("Judy"), true, 0). food("fish and chips"). st_hpd(order("Judy", "fish and chips", "the waiter"), true, 1). st_hpd(order_for("Judy", "Alex", "fish and chips", "the waiter"), true, 1). st_hpd(order_for("Judy", "Zoe", "fish and chips", "the waiter"), true, 1).
```

### Ground Truth
```clingo
restaurant("a local restaurant"). person("Judy"). person("Alex"). person("Zoe"). customer("they"). member("Judy", "they"). member("Alex", "they"). member("Zoe", "they"). food("fish and chips"). story_step(0..1). st_obs(sitting("they"), true, 0). st_hpd(order("they", "fish and chips", w), true, 1).
```

---

## Story #70 — Partial Match (Similarity: 0.0476)

**Story:** 

### Predicted
```clingo
restaurant("a pizzeria"). customer("the Jackson family"). waiter("the waiter"). food("a large pepperoni pizza"). beverage("a pitcher of soda"). st_hpd(lead_to("the waiter", "the Jackson family", t), true, 0). st_hpd(order("the Jackson family", "a large pepperoni pizza", "the waiter"), true, 1). st_hpd(order("the Jackson family", "a pitcher of soda", "the waiter"), true, 1). st_hpd(put_down("the waiter", "a large pepperoni pizza", t), true, 2). st_hpd(put_down("the waiter", "a pitcher of soda", t), true, 2).
```

### Ground Truth
```clingo
restaurant("pizzeria"). customer("The Jackson family"). food("large pepperoni pizza"). beverage("pitcher of soda"). waiter("the waiter"). st_hpd(enter("The Jackson family", "pizzeria"), true, 0). st_hpd(lead_to("the waiter", "The Jackson family", t), true, 1). st_hpd(order("The Jackson family", "large pepperoni pizza", "the waiter"), true, 2). st_hpd(order("The Jackson family", "pitcher of soda", "the waiter"), true, 2). st_hpd(put_down("the waiter", "large pepperoni pizza", t), true, 3). st_hpd(put_down("the waiter", "pitcher of soda", t), true, 3). st_hpd(eat("The Jackson family", "large pepperoni pizza"), true, 4).
```

---

## Story #77 — Partial Match (Similarity: 0.0500)

**Story:** [REDACTED — original ROCStories text; storyid=44b80dab-a351-4065-86b8-43d519dff470]

### Predicted
```clingo
restaurant("the new restaurant"). customer("Karl"). customer("his wife"). waiter("the waiter"). st_obs(sitting("Karl"), true, 0). st_obs(sitting("his wife"), true, 0). st_hpd(order("Karl"), false). st_hpd(order("his wife"), false). st_hpd(leave("Karl"), true, 1). st_hpd(leave("his wife"), true, 1).
```

### Ground Truth
```clingo
restaurant("new restaurant"). waiter("the waiter"). customer(they). person("Karl"). person("his wife"). member("Karl", they). member("his wife", they). waiter(w). st_obs(sitting(they), true, 0). st_hpd(served(they), false, 1). st_hpd(leave(they), true, 2).
```

---

## Story #15 — Partial Match (Similarity: 0.0556)

**Story:** 

### Predicted
```clingo
restaurant("fine restaurant"). customer("the villager"). waiter("the waiter"). st_hpd(enter("the villager", "fine restaurant"), true, 0). st_hpd(lead_to("the waiter", "the villager", t), true, 1). st_obs(sitting("the villager"), true, 2). st_hpd(read_menu("the villager"), true, 3). food("lettuce salad"). st_hpd(order("the villager", "lettuce salad", "the waiter"), true, 4). st_hpd(put_down("the waiter", "lettuce salad", t), true, 5).
```

### Ground Truth
```clingo
restaurant("a fine restaurant"). customer("the villager"). food("one of the items on the list"). food("lettuce salad with several black olives on top"). story_step(0..4). st_hpd(enter("the villager", "a fine restaurant"), true, 0). st_obs(sitting("the villager"), true, 1). st_hpd(pick_up("the villager", m, t), true, 2). st_hpd(order("the villager", "one of the items on the list", w), true, 3). st_hpd(put_down(w, "lettuce salad with several black olives on top", t), true, 4).
```

---

## Story #81 — Partial Match (Similarity: 0.0556)

**Story:** [REDACTED — original ROCStories text; storyid=1d235832-c133-4950-ba20-512adb2e3edb]

### Predicted
```clingo
restaurant("the new Italian restaurant"). customer("Kathy"). customer("her friend"). st_hpd(enter("Kathy", "the new Italian restaurant"), true, 0). st_hpd(enter("her friend", "the new Italian restaurant"), true, 0). food("dinner"). st_hpd(order("Kathy", "dinner", w), true, 1). st_hpd(order_for("Kathy", "her friend", "dinner", w), true, 1). st_hpd(eat("Kathy", "dinner"), true, 2). st_hpd(eat("her friend", "dinner"), true, 2).
```

### Ground Truth
```clingo
restaurant("new Italian restaurant"). customer(they). person("Kathy"). person("her friend"). member("Kathy", they). member("her friend", they). food("dinner"). st_hpd(enter(they, "new Italian restaurant"), true, 0). st_hpd(eat(they, "dinner"), true, 1).
```

---

## Story #90 — Partial Match (Similarity: 0.0625)

**Story:** [REDACTED — original ROCStories text; storyid=c4078b0f-e1c3-4c75-a05a-a52c9481fc2a]

### Predicted
```clingo
restaurant("restaurant on the Ohio river"). customer("I"). waiter("the waiter"). food(f). member("salmon", f). member("asparagus", f). st_hpd(enter("I", "restaurant on the Ohio river"), true, 0). st_hpd(order("I", f, "the waiter"), true, 1). st_hpd(eat("I", f), true, 2).
```

### Ground Truth
```clingo
restaurant("a restaurant"). customer("My family"). customer("I"). food("bread"). food("salmon and asparagus"). st_hpd(enter("My family", "a restaurant"), true, 0). st_hpd(eat("My family", "bread"), true, 1). st_hpd(eat("I", "salmon and asparagus"), true, 1).
```

---

## Story #24 — Partial Match (Similarity: 0.0741)

**Story:** 

### Predicted
```clingo
restaurant("a restaurant"). customer("Jasper"). customer("Frank"). waiter("the waiter"). food("roast beef"). beverage("coffee"). st_hpd(order("Jasper", "roast beef", "the waiter"), true, 0). st_hpd(order("Jasper", "coffee", "the waiter"), true, 0). st_hpd(put_down("the waiter", "coffee", t), true, 1). st_hpd(put_down("the waiter", "roast beef", t), true, 2). st_hpd(eat("Jasper", "roast beef"), true, 3). st_hpd(drink("Jasper", "coffee"), true, 3). st_hpd(eat("Frank", "roast beef"), true, 3). st_hpd(drink("Frank", "coffee"), true, 3). st_hpd(pay("Frank", b), true, 4).
```

### Ground Truth
```clingo
restaurant("a restaurant"). customer(they). member("Jasper", they). member("Frank", they). food(f). member("roast beef", f). member(coffee, f). waiter(w). story_step(0..4). st_hpd(enter(they, "a restaurant"), true, 0). st_hpd(order_for("Jasper", they, f, w), true, 1). st_hpd(put_down(w, f, t), true, 2). st_hpd(eat(they, f), true, 3). st_hpd(pay("Jasper", b), false, 4). st_hpd(pay("Frank", b), true, 4).
```

---

## Story #21 — Partial Match (Similarity: 0.0833)

**Story:** 

### Predicted
```clingo
restaurant("the restaurant"). customer("Emanuel"). customer("Ingrid"). waiter("the waiter"). beverage("wine"). food("gypsy shashlik"). st_hpd(put_down("the waiter", "wine", t), true, 0). st_hpd(read_menu("Emanuel"), true, 1). st_hpd(order("Emanuel", "gypsy shashlik", "the waiter"), true, 2). st_hpd(order_for("Emanuel", "Ingrid", "gypsy shashlik", "the waiter"), true, 2). st_hpd(drink("Emanuel", "wine"), true, 3). st_hpd(drink("Ingrid", "wine"), true, 3). st_hpd(put_down("the waiter", "gypsy shashlik", t), true, 4).
```

### Ground Truth
```clingo
restaurant(r). customer(they). member("Emanuel"). member("Ingrid"). drink(wine). food("gypsy shashlik"). waiter("the waiter"). story_step(0..5). st_hpd(put_down("the waiter", wine, t), true, 0). st_hpd(pick_up("Emanuel", m, t), true, 1). st_hpd(order_for("Emanuel", they, "gypsy shashlik", "the waiter"), true, 2). st_hpd(move("the waiter", t, kitchen), true, 3). st_hpd(drink(they, wine), true, 4). st_hpd(put_down("the waiter", "gypsy shashlik", t), true, 5).
```

---

## Story #92 — Partial Match (Similarity: 0.0833)

**Story:** [REDACTED — original ROCStories text; storyid=c9e533e3-d8cc-4e9c-a7a0-0369d6cdc537]

### Predicted
```clingo
restaurant("new restaurant in the mall"). customer("I"). waiter("the waiter"). food("a large salad"). st_hpd(order("I", "a large salad", "the waiter"), true, 0).
```

### Ground Truth
```clingo
restaurant("new restaurant"). customer("I"). food("large salad"). food("small salad"). waiter(w). st_obs(in("I", "new restaurant"), true, 0). st_hpd(order("I", "large salad", w), true, 1). st_hpd(put_down(w, "small salad", t), true, 2).
```

---

## Story #67 — Partial Match (Similarity: 0.0857)

**Story:** 

### Predicted
```clingo
restaurant("quiet Italian restaurant"). customer("Maria"). customer("Leo"). waiter("the waiter"). beverage("a bottle of red wine"). food("pasta dishes"). st_hpd(enter("Maria", "quiet Italian restaurant"), true, 0). st_hpd(enter("Leo", "quiet Italian restaurant"), true, 0). st_hpd(lead_to("the waiter", "Maria", t), true, 1). st_hpd(lead_to("the waiter", "Leo", t), true, 1). st_hpd(order("Maria", "a bottle of red wine", "the waiter"), true, 2). st_hpd(order_for("Maria", "Leo", "a bottle of red wine", "the waiter"), true, 2). st_hpd(put_down("the waiter", "a bottle of red wine", t), true, 3). st_hpd(order("Maria", "pasta dishes", "the waiter"), true, 4). st_hpd(order_for("Maria", "Leo", "pasta dishes", "the waiter"), true, 4). st_hpd(eat("Maria", "pasta dishes"), true, 5). st_hpd(eat("Leo", "pasta dishes"), true, 5). st_hpd(pay("Maria", b), true, 6). st_hpd(leave("Maria"), true, 7). st_hpd(leave("Leo"), true, 7).
```

### Ground Truth
```clingo
restaurant("quiet Italian restaurant"). customer(they). person("Maria"). person("Leo"). member("Maria", they). member("Leo", they). beverage("red wine"). food("pasta dishes"). waiter("the waiter"). story_step(0..7). st_hpd(enter(they, "quiet Italian restaurant"), true, 0). st_hpd(lead_to("the waiter", they, t), true, 1). st_hpd(order(they, "red wine", "the waiter"), true, 2). st_hpd(put_down("the waiter", "red wine", t), true, 3). st_hpd(order(they, "pasta dishes", "the waiter"), true, 4). st_hpd(eat(they, "pasta dishes"), true, 5). st_hpd(drink(they, "red wine"), true, 5). st_hpd(pay(they, b), true, 6). st_hpd(leave(they), true, 7).
```

---

## Story #45 — Partial Match (Similarity: 0.0909)

**Story:** 

### Predicted
```clingo
restaurant("the restaurant"). customer("the group of friends"). waiter("the waiter"). st_obs(sitting("the group of friends"), true, 0). st_hpd(order("the group of friends"), false). st_hpd(leave("the group of friends"), true, 1).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer("group of friends"). waiter(w). story_step(0..2). st_obs(sitting("group of friends"), true, 0). st_hpd(served("group of friends"), false). st_hpd(leave("group of friends"), true, 1).
```

---

## Story #88 — Partial Match (Similarity: 0.0909)

**Story:** [REDACTED — original ROCStories text; storyid=3a66621b-9dcf-4e32-b085-e4c0a2e89f8f]

### Predicted
```clingo
restaurant("the little deli on the corner"). customer("I"). waiter("the waiter"). food("a turkey sandwich"). st_hpd(order("I", "a turkey sandwich", "the waiter"), true, 0). st_hpd(eat("I", "a turkey sandwich"), true, 1).
```

### Ground Truth
```clingo
restaurant("little deli"). customer("I"). food("turkey sandwich"). st_obs(hungry("I"), true, 0). st_hpd(order("I", "turkey sandwich", w), true, 1). st_hpd(eat("I", "turkey sandwich"), true, 2).
```

---

## Story #28 — Partial Match (Similarity: 0.0952)

**Story:** 

### Predicted
```clingo
restaurant("RRGrill"). customer("Andy"). waiter("the waiter"). food("soup"). st_obs(open("RRGrill"), true, 0). st_hpd(enter("Andy", "RRGrill"), true, 1). st_hpd(greet("the waiter", "Andy"), true, 2). st_hpd(lead_to("the waiter", "Andy", t), true, 3). st_hpd(order("Andy", "soup", "the waiter"), true, 4). st_hpd(eat("Andy", "soup"), true, 5). st_hpd(pay("Andy", b), true, 6). st_hpd(leave("Andy"), true, 7).
```

### Ground Truth
```clingo
restaurant("RRGrill"). customer(andy). food(soup). waiter("the waiter"). story_step(0..4). st_hpd(enter(andy, "RRGrill"), true, 0). st_hpd(greet("the waiter", andy), true, 1). st_hpd(lead_to("the waiter", andy, t), true, 2). st_hpd(order(andy, soup, "the waiter"), true, 3). st_hpd(eat(andy, soup), true, 4). st_hpd(pay(andy, b), true, 5). st_hpd(leave(andy), true, 6).
```

---

## Story #19 — Partial Match (Similarity: 0.0968)

**Story:** 

### Predicted
```clingo
restaurant("the restaurant"). customer("Brand"). waiter("the waiter"). beverage("whiskey with Pepsi"). food(f). member("pyrogies", f). member("sausage cooked in sauerkraut", f). food("a large bowl of borscht"). st_hpd(order("Brand", f, "the waiter"), true, 0). st_hpd(order("Brand", "whiskey with Pepsi", "the waiter"), true, 0). st_hpd(put_down("the waiter", "whiskey with Pepsi", t), true, 1). st_hpd(put_down("the waiter", f, t), true, 2). st_hpd(request("Brand", "a large bowl of borscht", "the waiter"), true, 3). st_hpd(eat("Brand", "pyrogies"), true, 4). st_hpd(eat("Brand", "sausage cooked in sauerkraut"), true, 5). st_hpd(put_down("the waiter", "a large bowl of borscht", t), true, 6).
```

### Ground Truth
```clingo
restaurant(r). customer("Brand"). beverage("whiskey with Pepsi, no ice"). food(f). member(pyrogies, f). member("sausage in sauerkraut", f). food(borscht). waiter("the waiter"). story_step(0..9). st_hpd(sit("Brand"), true, 0). st_hpd(pick_up("Brand", m, t), true, 1). st_hpd(order("Brand", "whiskey with Pepsi, no ice", "the waiter"), true, 2). st_hpd(order("Brand", f, "the waiter"), true, 3). st_hpd(put_down("the waiter", "whiskey with Pepsi, no ice"), t), true, 4). st_hpd(put_down("the waiter", f, t), true, 5). st_hpd(order("Brand", borscht, "the waiter"), true, 6). st_hpd(move("the waiter", t, kitchen), true, 7). st_hpd(eat("Brand", f), true, 8). st_hpd(put_down("the waiter", borscht, t), true, 9).
```

---

## Story #56 — Partial Match (Similarity: 0.1053)

**Story:** 

### Predicted
```clingo
restaurant("vegan restaurant downtown"). customer("Anna"). waiter("the waiter"). food("quinoa bowl"). beverage("a green smoothie"). st_hpd(order("Anna", "quinoa bowl", "the waiter"), true, 0). st_hpd(order("Anna", "a green smoothie", "the waiter"), true, 0). st_hpd(pay("Anna", tip), true, 1).
```

### Ground Truth
```clingo
restaurant("vegan restaurant"). customer("Anna"). food("quinoa bowl"). beverage("green smoothie"). waiter(w). story_step(0..4). st_hpd(enter("Anna", "vegan restaurant"), true, 0). st_hpd(order("Anna", "quinoa bowl", w), true, 1). st_hpd(order("Anna", "green smoothie", w), true, 1). st_hpd(put_down("the waiter", "quinoa bowl", t), true, 2). st_hpd(put_down("the waiter", "green smoothie", t), true, 2). st_hpd(eat("Anna", "quinoa bowl"), true, 3). st_hpd(drink("Anna", "green smoothie"), true, 3). st_hpd(pay("Anna", tip), true, 4).
```

---

## Story #96 — Partial Match (Similarity: 0.1053)

**Story:** [REDACTED — original ROCStories text; storyid=77710d2a-dbc2-4c99-a892-190b529ad219]

### Predicted
```clingo
restaurant("fast food restaurant"). customer("Dina"). customer("her friend"). waiter("the waiter"). food("fries"). st_hpd(order("Dina", "fries", "the waiter"), true, 0). st_hpd(order_for("Dina", "her friend", "fries", "the waiter"), true, 0). st_hpd(eat("Dina", "fries"), true, 1).
```

### Ground Truth
```clingo
restaurant("fast food restaurant"). customer(they). person("Dina"). person("a friend"). member("Dina", they). member("a friend", they). food("fries"). st_obs(in("Dina", "fast food restaurant"), true, 0). st_obs(hungry("Dina"), false, 1). st_hpd(order(they, "fries", w), true, 2). st_hpd(pay("Dina", b), true, 3). st_hpd(pay("a friend", b), true, 3). st_hpd(eat("Dina", "fries"), true, 4).
```

---

## Story #12 — Partial Match (Similarity: 0.1154)

**Story:** 

### Predicted
```clingo
restaurant("famous restaurant"). customer("I"). customer("my husband"). waiter("the waiter"). food(f). member("escargot", f). member("lamb", f). member("savory salmon", f). member("creamy flan dessert", f). st_hpd(enter("I", "famous restaurant"), true, 0). st_hpd(enter("my husband", "famous restaurant"), true, 0). st_obs(sitting("I"), true, 1). st_obs(sitting("my husband"), true, 1). st_hpd(read_menu("I"), true, 2). st_hpd(order("I", f, "the waiter"), true, 3).
```

### Ground Truth
```clingo
restaurant("a famous restaurant"). person("my husband"). person("I"). customer("we"). member("my husband", "we"). member("I", "we"). member("escargot", f). member("lamb", f). member("savory salmon", f). member("creamy flan dessert", f) story_step(0..3). st_hpd(enter("we", "a famous restaurant"), true, 0). st_obs(sitting("we"), true, 1). st_hpd(read_menu("we"), true, 2). st_hpd(order("we", f, w), true, 3).
```

---

## Story #80 — Partial Match (Similarity: 0.1154)

**Story:** [REDACTED — original ROCStories text; storyid=d85b7ce5-0d84-4181-afe4-52c64711145a]

### Predicted
```clingo
restaurant("Genki Ya"). customer("I"). customer("my son"). waiter("the waiter"). beverage("Japanese beers"). food(f). member("fish roe", f). member("two combo sashimi-sushi dishes", f). st_hpd(enter("I", "Genki Ya"), true, 0). st_hpd(enter("my son", "Genki Ya"), true, 0). st_hpd(order("I", f, "the waiter"), true, 1). st_hpd(order("I", "Japanese beers", "the waiter"), true, 1). st_hpd(eat("I", f), true, 2). st_hpd(eat("my son", f), true, 2). st_hpd(drink("I", "Japanese beers"), true, 2). st_hpd(drink("my son", "Japanese beers"), true, 2).
```

### Ground Truth
```clingo
restaurant("Genki Ya"). customer(we). person("my son"). person("I"). member("my son", we). member("I", we). beverage("japanese beers"). food(f). member("fish roe", f). member("sashimi-sushi dishes", f). st_hpd(enter(we, "Genki Ya"), true, 0). st_hpd(eat(we, f), true, 2). st_hpd(drink(we, "japanese beers"), true, 2).
```

---

## Story #23 — Partial Match (Similarity: 0.1200)

**Story:** 

### Predicted
```clingo
restaurant("the restaurant"). customer("I"). waiter("the waiter"). beverage("red wine"). food("salmon"). food("a small plate of hors d'oeuvres"). st_hpd(read_menu("I"), true, 0). st_hpd(order("I", "salmon", "the waiter"), true, 1). st_hpd(put_down("the waiter", "red wine", t), true, 2). st_hpd(drink("I", "red wine"), true, 3). st_hpd(put_down("the waiter", "a small plate of hors d'oeuvres", t), true, 4). st_hpd(eat("I", "a small plate of hors d'oeuvres"), true, 5). st_hpd(put_down("the waiter", "salmon", t), true, 6). st_hpd(eat("I", "salmon"), true, 7).
```

### Ground Truth
```clingo
restaurant(r). customer("I"). food(salmon). drink("red wine"). food("hors d'oeuvres"). waiter("the waiter"). story_step(0..7). st_hpd(pick_up("I", m, t), true, 0). st_hpd(order("I", salmon, "the waiter"), true, 1). st_hpd(put_down("I", "red wine", t), true, 2). st_hpd(drink("I", "red wine"), true, 3). st_hpd(put_down("the waiter", "hors d'oeuvres", t), true, 4). st_hpd(eat("I", "hors d'oeuvres"), true, 5). st_hpd(put_down("the waiter", salmon, t), true, 6). st_hpd(eat("I", salmon), true, 7).
```

---

## Story #51 — Partial Match (Similarity: 0.1250)

**Story:** 

### Predicted
```clingo
restaurant("pizzeria"). customer("Steve"). customer("his son"). waiter("the waiter"). food("a large pepperoni pizza"). st_hpd(enter("Steve", "pizzeria"), true, 0). st_hpd(enter("his son", "pizzeria"), true, 0). st_hpd(lead_to("the waiter", "Steve", t), true, 1). st_hpd(lead_to("the waiter", "his son", t), true, 1). st_hpd(order("Steve", "a large pepperoni pizza", "the waiter"), true, 2). st_hpd(order_for("Steve", "his son", "a large pepperoni pizza", "the waiter"), true, 2). st_hpd(eat("Steve", "a large pepperoni pizza"), true, 3). st_hpd(eat("his son", "a large pepperoni pizza"), true, 3). st_hpd(pay("Steve", b), true, 4).
```

### Ground Truth
```clingo
restaurant("pizzeria"). customer(they). person("Steve"). person("his son"). member("Steve", they). member("his son", they). food("large pepperoni pizza"). waiter("the waiter"). story_step(0..4). st_hpd(enter(they, "pizzeria"), true, 0). st_hpd(lead_to("the waiter", they, t), true, 1). st_hpd(order(they, "large pepperoni pizza", "the waiter"), true, 2). st_hpd(eat(they, "large pepperoni pizza"), true, 3). st_hpd(pay("Steve", b), true, 4).
```

---

## Story #61 — Partial Match (Similarity: 0.1250)

**Story:** 

### Predicted
```clingo
restaurant("quiet cafe"). customer("the book club members"). waiter("the waiter"). beverage("various teas"). food("pastries"). st_hpd(order("the book club members", "various teas", "the waiter"), true, 0). st_hpd(order("the book club members", "pastries", "the waiter"), true, 0). st_hpd(drink("the book club members", "various teas"), true, 1). st_hpd(eat("the book club members", "pastries"), true, 1).
```

### Ground Truth
```clingo
restaurant("quiet cafe"). customer("book club members"). food("pastries"). beverage("teas"). story_step(0..2). st_hpd(enter("book club members", "quiet cafe"), true, 0). st_hpd(order("book club members", "pastries", "the waiter"), true, 1). st_hpd(order("book club members", "teas", "the waiter"), true, 1). st_hpd(eat("book club members", "pastries"), true, 2). st_hpd(drink("book club members", "teas"), true, 2).
```

---

## Story #76 — Partial Match (Similarity: 0.1250)

**Story:** [REDACTED — original ROCStories text; storyid=6ead4a09-8e5f-4fbc-8a32-b706bdbb7a87]

### Predicted
```clingo
restaurant("Allston Diner"). customer("we"). customer("our son"). waiter("the waiter"). customer("a friend"). food("large, hearty breakfast meals"). st_hpd(enter("we", "Allston Diner"), true, 0). st_hpd(order("we", "large, hearty breakfast meals", "the waiter"), true, 1). st_hpd(eat("we", "large, hearty breakfast meals"), true, 2).
```

### Ground Truth
```clingo
restaurant("Allston Diner"). customer(we). person("our son"). customer("a friend"). member("our son", we). food("breakfast meals"). st_hpd(enter(we, "Allston Diner"), true, 0). st_hpd(eat(we, "breakfast meals"), true, 1). st_hpd(eat("a friend", "breakfast meals"), true, 1).
```

---

## Story #89 — Partial Match (Similarity: 0.1250)

**Story:** [REDACTED — original ROCStories text; storyid=c93ca5db-716f-4572-868e-bd22aa4a9018]

### Predicted
```clingo
restaurant("Genki Ya"). customer("my son"). customer("me"). waiter("the waiter"). food("sashimi"). st_hpd(enter("my son", "Genki Ya"), true, 0). st_hpd(enter("me", "Genki Ya"), true, 0). st_hpd(order("me", "sashimi", "the waiter"), true, 1). st_hpd(eat("me", "sashimi"), true, 2).
```

### Ground Truth
```clingo
restaurant("Genki Ya"). customer(we). person("my son"). person("me"). member("my son", we). member("me", we). food("sashimi"). st_hpd(enter(we, "Genki Ya"), true, 0). st_hpd(eat(we, "sashimi"), true, 1).
```

---

## Story #97 — Partial Match (Similarity: 0.1250)

**Story:** [REDACTED — original ROCStories text; storyid=d25ec012-9f9f-48e6-8274-e6ac4a4b59e4]

### Predicted
```clingo
restaurant("the restaurant"). customer("Tim"). waiter("the waiter"). food("the wrong order"). food("the correct order"). st_hpd(put_down("the waiter", "the wrong order", t), true, 0). st_hpd(complain("Tim", "the waiter"), true, 1). st_hpd(pick_up("the waiter", "the wrong order", t), true, 2). st_hpd(put_down("the waiter", "the correct order", t), true, 3).
```

### Ground Truth
```clingo
restaurant(r). customer("Tim"). food("wrong order"). waiter("the waiter"). st_obs(in("Tim", r), true, 0). st_hpd(put_down("the waiter", "wrong order", t), true, 1). st_hpd(complain("Tim", "the waiter"), true, 2). st_next(1, 2). st_hpd(put_down("the waiter", f, t), true, 3).
```

---

## Story #14 — Partial Match (Similarity: 0.1429)

**Story:** 

### Predicted
```clingo
restaurant("five-star restaurant"). customer("Samantha"). waiter("the waiter"). st_obs(in("Samantha", "five-star restaurant"), true, 0). st_hpd(read_menu("Samantha"), true, 1). food(f). member("barbecued veal chop", f). member("Asian slaw", f). member("Thai fried rice", f). st_hpd(order("Samantha", f, "the waiter"), true, 2).
```

### Ground Truth
```clingo
restaurant("a five-star restaurant"). customer("Samantha"). food("barbecued veal chop with Asian slaw and Thai fried rice"). story_step(0..2). st_obs(in("Samantha", "a five-star restaurant"), true, 0). st_hpd(read_menu("Samantha"), true, 1). st_hpd(order("Samantha", "barbecued veal chop with Asian slaw and Thai fried rice", w), true, 2).
```

---

## Story #55 — Partial Match (Similarity: 0.1429)

**Story:** 

### Predicted
```clingo
restaurant("sushi restaurant"). customer("Mark"). customer("Lisa"). waiter("the waiter"). food("tuna rolls"). food("salmon nigiri"). st_obs(at_l("Mark", "the sushi bar"), true, 0). st_obs(at_l("Lisa", "the sushi bar"), true, 0). st_hpd(order("Mark", "tuna rolls", "the waiter"), true, 1). st_hpd(order("Lisa", "salmon nigiri", "the waiter"), true, 1).
```

### Ground Truth
```clingo
restaurant("sushi restaurant"). waiter(w). person("Mark"). person("Lisa"). customer("they"). member("Mark", "they"). member("Mark", "they"). food("tuna rolls"). food("salmon nigiri"). story_step(0..4). st_hpd(enter("they", "sushi restaurant"), true, 0). st_obs(sitting("they"), true, 1). st_hpd(order("Mark", "tuna rolls", w), true, 2). st_hpd(order("Lisa", "salmon nigiri", w), true, 2). st_hpd(prepare("the chef", "tuna rolls", w), true, 3). st_hpd(prepare("the chef", "salmon nigiri", w), true, 3).
```

---

## Story #74 — Partial Match (Similarity: 0.1429)

**Story:** 

### Predicted
```clingo
restaurant("the Italian restaurant"). customer("Lisa"). customer("Mark"). waiter("the waiter"). food("lasagna"). food("chicken parmesan"). beverage("a bottle of wine"). st_hpd(lead_to("the waiter", "Lisa", t), true, 0). st_hpd(lead_to("the waiter", "Mark", t), true, 0). st_hpd(order("Lisa", "lasagna", "the waiter"), true, 1). st_hpd(order("Mark", "chicken parmesan", "the waiter"), true, 1). st_hpd(order("Lisa", "a bottle of wine", "the waiter"), true, 2). st_hpd(order_for("Lisa", "Mark", "a bottle of wine", "the waiter"), true, 2). st_hpd(put_down("the waiter", "a bottle of wine", t), true, 3). st_hpd(drink("Lisa", "a bottle of wine"), true, 4). st_hpd(drink("Mark", "a bottle of wine"), true, 4).
```

### Ground Truth
```clingo
restaurant("Italian restaurant"). customer("Lisa"). customer("Mark"). customer(they). member("Lisa", they). member("Mark", they). food("lasagna"). food("chicken parmesan"). beverage("wine"). st_hpd(enter(they, "Italian restaurant"), true, 0). st_obs(sitting(they), true, 1). st_hpd(order("Lisa", "lasagna", "the waiter"), true, 2). st_hpd(order("Mark", "chicken parmesan", "the waiter"), true, 2). st_hpd(eat("Lisa", "lasagna"), true, 3). st_hpd(eat("Mark", "chicken parmesan"), true, 3). st_hpd(drink(they, "wine"), true, 3).
```

---

## Story #86 — Partial Match (Similarity: 0.1429)

**Story:** [REDACTED — original ROCStories text; storyid=541efb12-b331-4525-afe1-5422ff33a1ca]

### Predicted
```clingo
restaurant("the diner"). customer("Samuel"). customer("John"). waiter("the waiter"). food("a hamburger without onions"). food("a hotdog"). st_hpd(order("Samuel", "a hamburger without onions", "the waiter"), true, 0). st_hpd(put_down("the waiter", "a hotdog", t), true, 1). st_hpd(complain("Samuel", "the waiter"), true, 2). st_next(1,2). st_hpd(put_down("the waiter", "a hamburger without onions", t), true, 3).
```

### Ground Truth
```clingo
restaurant("diner"). customer("Samuel"). customer("John"). food("hamburger without onions"). food("hotdog"). waiter("the waiter"). st_obs(in("Samuel", "diner"), true, 0). st_obs(in("John", "diner"), true, 0). st_hpd(order("Samuel", "hamburger without onions", "the waiter"), true, 1). st_hpd(put_down("the waiter", "hotdog", t), true, 2). st_hpd(complain("Samuel", "the waiter"), true, 3). st_next(2,3). st_hpd(put_down("the waiter", "hamburger without onions", t), true, 4).
```

---

## Story #36 — Partial Match (Similarity: 0.1538)

**Story:** 

### Predicted
```clingo
restaurant("RRGrill"). customer("Andy"). customer("Tom"). waiter("the waiter"). st_obs(open("RRGrill"), true, 0). st_hpd(lead_to("the waiter", "Andy", t), true, 1).
```

### Ground Truth
```clingo
restaurant("RRGrill"). customer("Andy"). person("Tom"). food("all the food"). waiter("the waitress"). story_step(0..2). st_hpd(enter("Andy", "RRGrill"), true, 0). st_hpd(lead_to("waitress", "Andy", t), true, 1). st_obs(informed("the waitress", "all the food", "Andy"), true, 2). st_hpd(pay("Tom", b), 2).
```

---

## Story #69 — Partial Match (Similarity: 0.1765)

**Story:** 

### Predicted
```clingo
restaurant("sandwich shop"). customer("the coworkers"). waiter("the waiter"). food("sandwiches"). st_hpd(lead_to("the waiter", "the coworkers", t), true, 0). st_hpd(order("the coworkers", "sandwiches", "the waiter"), true, 1). st_hpd(put_down("the waiter", "sandwiches", t), true, 2). st_hpd(eat("the coworkers", "sandwiches"), true, 3). st_hpd(pay("the coworkers", b), true, 4).
```

### Ground Truth
```clingo
restaurant("sandwich shop"). customer("group of coworkers"). food("sandwiches"). waiter("the waiter"). st_hpd(enter("group of coworkers", "sandwich shop"), true, 0). st_hpd(lead_to("the waiter", "group of coworkers", t), true, 1). st_hpd(order("group of coworkers", "sandwiches", "the waiter"), true, 2). st_hpd(put_down("the waiter", "sandwiches", t), true, 3). st_hpd(eat("group of coworkers", "sandwiches"), true, 4). st_hpd(pay("group of coworkers", b), true, 5). st_hpd(leave("group of coworkers"), true, 6).
```

---

## Story #71 — Partial Match (Similarity: 0.1818)

**Story:** 

### Predicted
```clingo
restaurant("the bistro"). customer("Michael"). waiter("the waitress"). food("the daily special"). beverage("a glass of water"). st_hpd(enter("Michael", "the bistro"), true, 0). st_hpd(lead_to("the waitress", "Michael", t), true, 1). st_hpd(order("Michael", "the daily special", "the waitress"), true, 2). st_hpd(order("Michael", "a glass of water", "the waitress"), true, 2). st_hpd(put_down("the waitress", "the daily special", t), true, 3). st_hpd(put_down("the waitress", "a glass of water", t), true, 3). st_hpd(request("Michael", b, "the waitress"), true, 4).
```

### Ground Truth
```clingo
restaurant("the bistro"). customer("Michael"). food("daily special"). beverage("water"). waiter("the waitress"). st_hpd(enter("Michael", "the bistro"), true, 0). st_hpd(lead_to("the host", "Michael", t), true, 1). st_hpd(order("Michael", "daily special", "the waitress"), true, 2). st_hpd(order("Michael", "water", "the waitress"), true, 2). st_hpd(put_down("the waitress", "daily special", t), true, 3). st_hpd(put_down("the waitress", "water", t), true, 3). st_hpd(eat("Michael", "daily special"), true, 4). st_hpd(drink("Michael", "water"), true, 4). st_hpd(request("Michael", b, "the waitress"), true, 5).
```

---

## Story #79 — Partial Match (Similarity: 0.1818)

**Story:** [REDACTED — original ROCStories text; storyid=845b62e4-9240-4afe-8d59-ae2bc183967c]

### Predicted
```clingo
restaurant("a new steakhouse"). customer("the couple"). waiter("the waiter"). food("huge cuts of meat"). st_hpd(order("the couple", "huge cuts of meat", "the waiter"), true, 0). st_hpd(read_bill("the couple"), true, 1).
```

### Ground Truth
```clingo
restaurant("new steakhouse"). customer("the couple"). food("huge cuts of meat"). st_obs(in("the couple", "new steakhouse"), true, 0). st_hpd(put_down(w, "huge cuts of meat", t), true, 1). st_hpd(eat("the couple", "huge cuts of meat"), true, 2). st_hpd(put_down(w, b, t), true, 3).
```

---

## Story #47 — Partial Match (Similarity: 0.1875)

**Story:** 

### Predicted
```clingo
restaurant("the restaurant"). customer("Gary"). waiter("the waiter"). food("steak"). food("a small cake"). st_hpd(enter("Gary", "the restaurant"), true, 0). st_hpd(order("Gary", "steak", "the waiter"), true, 1). st_hpd(eat("Gary", "steak"), true, 2). st_hpd(put_down("the waiter", "a small cake", t), true, 3). st_hpd(pay("Gary", tip), true, 4).
```

### Ground Truth
```clingo
restaurant("a restaurant"). customer("Gary"). food("steak"). food("cake"). waiter("the waiter"). story_step(0..3). st_hpd(order("Gary", "steak", "the waiter"), true, 0). st_hpd(eat("Gary", "steak"), true, 1). st_hpd(put_down("the waiter", "cake", t), true, 2). st_hpd(pay("Gary", tip), true, 3).
```

---

## Story #91 — Partial Match (Similarity: 0.1875)

**Story:** [REDACTED — original ROCStories text; storyid=ac7250f9-d416-41bb-aac7-b1dd788b86fb]

### Predicted
```clingo
restaurant("fast food restaurant"). customer("Emily"). waiter("the cashier"). food(f). member("fries", f). member("a burger", f). st_hpd(order("Emily", f, "the cashier"), true, 0). st_obs(informed("Emily", "order missing fries", "the cashier"), true, 1).
```

### Ground Truth
```clingo
restaurant("fast food restaurant"). customer("Emily"). food("fries"). food("burger"). waiter("the cashier"). st_hpd(order("Emily", "fries", "the cashier"), true, 0). st_hpd(order("Emily", "burger", "the cashier"), true, 0). st_hpd(put_down("the cashier", "burger", t), true, 1). st_hpd(put_down("the cashier", "fries", t), false). st_hpd(complain("Emily", "the cashier"), true, 2). st_next(1,2).
```

---

## Story #42 — Partial Match (Similarity: 0.2000)

**Story:** 

### Predicted
```clingo
restaurant("fancy restaurant"). customer("David"). customer("Sarah"). waiter("the waiter"). food("duck confit"). beverage("wine"). st_hpd(enter("David", "fancy restaurant"), true, 0). st_hpd(enter("Sarah", "fancy restaurant"), true, 0). st_hpd(order("David", "duck confit", "the waiter"), true, 1). st_hpd(order_for("David", "Sarah", "duck confit", "the waiter"), true, 1). st_hpd(put_down("the waiter", "duck confit", t), true, 2). st_hpd(put_down("the waiter", "wine", t), true, 2). st_hpd(eat("David", "duck confit"), true, 3). st_hpd(eat("Sarah", "duck confit"), true, 3). st_hpd(drink("David", "wine"), true, 3). st_hpd(drink("Sarah", "wine"), true, 3).
```

### Ground Truth
```clingo
restaurant("fancy restaurant"). customer(they). person("David"). person("Sarah"). member("David", they). member("Sarah", they). food("duck confit"). beverage("wine"). waiter("the waiter"). story_step(0..3). st_hpd(order_for("David", they, "duck confit", "the waiter"), true, 0). st_hpd(put_down("the waiter", "duck confit", t), true, 1). st_hpd(put_down("the waiter", "wine", t), true, 2). st_hpd(eat(they, "duck confit"), true, 3). st_hpd(drink(they, "wine"), true, 3).
```

---

## Story #57 — Partial Match (Similarity: 0.2000)

**Story:** 

### Predicted
```clingo
restaurant("Mexican restaurant"). customer("Carlos"). waiter("the waiter"). food("tacos"). beverage("a margarita"). st_hpd(enter("Carlos", "Mexican restaurant"), true, 0). st_hpd(greet("the waiter", "Carlos"), true, 1). st_hpd(order("Carlos", "tacos", "the waiter"), true, 2). st_hpd(order("Carlos", "a margarita", "the waiter"), true, 2). st_hpd(eat("Carlos", "tacos"), true, 3). st_hpd(drink("Carlos", "a margarita"), true, 3).
```

### Ground Truth
```clingo
restaurant("Mexican restaurant"). customer("Carlos"). waiter(w). food("tacos"). beverage("margarita"). story_step(0..4). st_hpd(enter("Carlos", "Mexican restaurant"), true, 0). st_hpd(greet(w, "Carlos"), true, 1). st_hpd(order("Carlos", "tacos", w), true, 2). st_hpd(order("Carlos", "margarita", w), true, 2). st_hpd(put_down(w, "tacos", t), true, 3). st_hpd(put_down(w, "margarita", t), true, 3). st_hpd(eat("Carlos", "tacos"), true, 4). st_hpd(drink("Carlos", "margarita"), true, 4).
```

---

## Story #83 — Partial Match (Similarity: 0.2000)

**Story:** [REDACTED — original ROCStories text; storyid=9c2ccb82-003d-4253-9f19-65b157b9993f]

### Predicted
```clingo
restaurant("the diner"). customer("the couple"). waiter("the waitress"). st_obs(sitting("the couple"), true, 0). st_hpd(order("the couple"), false). st_hpd(leave("the couple"), true, 1).
```

### Ground Truth
```clingo
restaurant("diner"). customer("the couple"). waiter("the waitress"). st_hpd(sit("the couple"), true, 0). st_hpd(greet("the waitress", "the couple"), false). st_hpd(stand_up("the couple"), true, 1).
```

---

## Story #54 — Partial Match (Similarity: 0.2105)

**Story:** 

### Predicted
```clingo
restaurant("the cafe"). customer("Sarah"). waiter("the waitress"). food("a chicken sandwich"). beverage("coffee"). st_hpd(sit("Sarah"), true, 0). st_hpd(order("Sarah", "a chicken sandwich", "the waitress"), true, 1). st_hpd(order("Sarah", "coffee", "the waitress"), true, 1). st_hpd(put_down("the waitress", "a chicken sandwich", t), true, 2). st_hpd(put_down("the waitress", "coffee", t), true, 2). st_hpd(eat("Sarah", "a chicken sandwich"), true, 3). st_hpd(drink("Sarah", "coffee"), true, 3).
```

### Ground Truth
```clingo
restaurant("the cafe"). customer("Sarah"). food("chicken sandwich"). beverage("coffee"). waiter("the waitress"). story_step(0..4). st_hpd(enter("Sarah", "the cafe"), true, 0). st_hpd(sit("Sarah"), true, 1). st_hpd(order("Sarah", "chicken sandwich", "the waitress"), true, 2). st_hpd(put_down("the waitress", "chicken sandwich", t), true, 3). st_hpd(eat("Sarah", "chicken sandwich"), true, 4). st_hpd(drink("Sarah", "coffee"), true, 4).
```

---

## Story #75 — Partial Match (Similarity: 0.2105)

**Story:** [REDACTED — original ROCStories text; storyid=99d073a9-375a-45ad-a070-0fdfbbf73f69]

### Predicted
```clingo
restaurant("new Sushi place"). customer("I"). customer("my husband"). waiter("the waiter"). food(f). member("spicy tuna rolls", f). member("eel", f). st_hpd(order("I", f, "the waiter"), true, 0). st_hpd(order_for("I", "my husband", f, "the waiter"), true, 0). st_hpd(eat("I", f), true, 1). st_hpd(eat("my husband", f), true, 1).
```

### Ground Truth
```clingo
restaurant("new Sushi place"). customer(we). person("I"). person("my husband"). member("I", we). member("my husband", we). food(f). member("spicy tuna rolls", f). member("eel", f). st_hpd(enter(we, "new Sushi place"), true, 0). st_hpd(order(we, f, w), true, 1). st_hpd(eat(we, f), true, 2).
```

---

## Story #22 — Partial Match (Similarity: 0.2174)

**Story:** 

### Predicted
```clingo
restaurant("a restaurant"). customer("Andrew"). customer("Sebastian"). waiter("the waiter"). beverage("a bottle of wine"). st_obs(sitting("Andrew"), true, 0). st_hpd(enter("Sebastian", "a restaurant"), true, 1). st_hpd(sit("Sebastian"), true, 2). st_hpd(put_down("the waiter", "a bottle of wine", t), true, 3). st_hpd(drink("Andrew", "a bottle of wine"), true, 4). st_hpd(drink("Sebastian", "a bottle of wine"), true, 4). st_hpd(read_menu("Andrew"), true, 5). st_hpd(read_menu("Sebastian"), true, 5).
```

### Ground Truth
```clingo
restaurant("a restaurant"). customer("the men"). person("Andrew"). person("Sebastian"). member("Andrew", "the men"). member("Sebastian", "the men"). drink(wine). waiter("the waiter"). story_step(0..5). st_obs(in("Andrew", "a restaurant"), true, 0). st_obs(sitting("Andrew"), true, 0). st_hpd(enter("Sebastian", "a restaurant"), true, 1). st_hpd(sit("Sebastian"), true, 2). st_hpd(put_down("the waiter", wine, t), true, 3). st_hpd(drink("the men", wine), true, 4). st_hpd(put_down("the waiter", m, t), true, 5).
```

---

## Story #72 — Partial Match (Similarity: 0.2222)

**Story:** 

### Predicted
```clingo
restaurant("pancake house"). customer("Susan"). waiter("the server"). food("blueberry pancakes"). beverage("orange juice"). st_hpd(order("Susan", "blueberry pancakes", "the server"), true, 0). st_hpd(order("Susan", "orange juice", "the server"), true, 0). st_hpd(put_down("the server", "blueberry pancakes", t), true, 1). st_hpd(put_down("the server", "orange juice", t), true, 1). st_hpd(eat("Susan", "blueberry pancakes"), true, 2). st_hpd(pay("Susan", b), true, 3).
```

### Ground Truth
```clingo
restaurant("the pancake house"). customer("Susan"). food("blueberry pancakes"). beverage("orange juice"). waiter("the server"). st_hpd(enter("Susan", "the pancake house"), true, 0). st_hpd(order("Susan", "blueberry pancakes", "the server"), true, 1). st_hpd(order("Susan", "orange juice", "the server"), true, 1). st_hpd(put_down("the server", "blueberry pancakes", t), true, 2). st_hpd(eat("Susan", "blueberry pancakes"), true, 3). st_hpd(pay("Susan", b), true, 4).
```

---

## Story #84 — Partial Match (Similarity: 0.2308)

**Story:** [REDACTED — original ROCStories text; storyid=0f9b69ff-6fbe-4e94-a37a-8ef3fbf2a876]

### Predicted
```clingo
restaurant("the diner"). customer("Donna"). waiter("the waiter"). food(f). member("the cheeseburger", f). member("onion rings", f). st_hpd(order("Donna", f, "the waiter"), true, 0). st_hpd(eat("Donna", f), true, 1).
```

### Ground Truth
```clingo
restaurant("diner"). customer("Donna"). food(f). member("cheeseburger", f). member("onion rings", f). st_hpd(enter("Donna", "diner"), true, 0). st_hpd(order("Donna", f, w), true, 1). st_hpd(eat("Donna", f), true, 2).
```

---

## Story #87 — Partial Match (Similarity: 0.2308)

**Story:** [REDACTED — original ROCStories text; storyid=7dc0c96f-dd24-4561-9a4f-bd1b6b3ca520]

### Predicted
```clingo
restaurant("the restaurant"). customer("I"). waiter("the waiter"). st_hpd(enter("I", "the restaurant"), true, 0). food("the wrong order"). st_hpd(put_down("the waiter", "the wrong order", t), true, 1). st_hpd(complain("I", "the waiter"), true, 2). st_hpd(pick_up("the waiter", "the wrong order", t), true, 3).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer("I"). food("wrong order"). st_hpd(enter("I", "the restaurant"), true, 0). st_hpd(order("I", f, w), true, 1). st_hpd(put_down(w, "wrong order", t), true, 2). st_hpd(request("I", pick_up(w, "burnt pizza", t), w), true, 3). st_next(2,3).
```

---

## Story #58 — Partial Match (Similarity: 0.2353)

**Story:** 

### Predicted
```clingo
restaurant("the diner"). customer("Ben"). waiter("the waiter"). beverage("coffee"). food(f). member("pancakes", f). member("bacon", f). st_hpd(enter("Ben", "the diner"), true, 0). st_obs(at_l("Ben", "the counter"), true, 1). st_hpd(order("Ben", f, "the waiter"), true, 2). st_hpd(order("Ben", "coffee", "the waiter"), true, 2). st_hpd(prepare("the cook", f, "the waiter"), true, 3).
```

### Ground Truth
```clingo
restaurant("the diner"). customer("Ben"). food("pancakes with bacon"). beverage("coffee"). story_step(0..3). st_hpd(enter("Ben", "the diner"), true, 0). st_hpd(sit("Ben"), true, 1). st_hpd(order("Ben", "pancakes with bacon", w), true, 2). st_hpd(prepare("the cook", "pancakes with bacon", w), true, 3). st_hpd(prepare("the cook", "coffee", "Ben"), true, 3).
```

---

## Story #35 — Partial Match (Similarity: 0.2500)

**Story:** 

### Predicted
```clingo
restaurant("RRGrill"). customer("Andy"). st_obs(open("RRGrill"), true, 0). st_hpd(leave("Andy"), true, 1).
```

### Ground Truth
```clingo
restaurant("RRGrill"). customer("Andy"). story_step(0..2). st_hpd(enter("Andy", "RRGrill"), true, 0). st_obs(table_available, false, 1). stop_activity("Andy", 1). st_hpd(leave("Andy"), true, 2).
```

---

## Story #49 — Partial Match (Similarity: 0.2500)

**Story:** 

### Predicted
```clingo
restaurant("the restaurant"). customer("Mark"). waiter("the waiter"). st_hpd(put_down("the waiter", b, t), true, 0). st_hpd(read_bill("Mark"), true, 1). st_hpd(order("Mark", "dessert", "the waiter"), false). st_hpd(complain("Mark", "the waiter"), true, 2). st_next(1,2).
```

### Ground Truth
```clingo
restaurant(r). customer("Mark"). food("dessert"). waiter("the waiter"). st_hpd(put_down("the waiter", b, t), true, 0). st_hpd(pick_up("Mark", b, t), true, 1). st_hpd(request("Mark", "correction", "the waiter"), true, 1).
```

---

## Story #85 — Partial Match (Similarity: 0.2500)

**Story:** [REDACTED — original ROCStories text; storyid=9915e783-6bf9-4d92-9150-b031bf778bb7]

### Predicted
```clingo
restaurant("a restaurant"). customer("I"). food("pizza"). st_hpd(order("I", "pizza", w), true, 0). st_hpd(put_down(w, "pizza", t), true, 1). st_hpd(complain("I", w), true, 2). st_hpd(pick_up(w, "pizza", t), true, 3).
```

### Ground Truth
```clingo
restaurant("a restaurant"). customer("I"). food("pizza"). food("burnt pizza"). st_hpd(enter("I", r), true, 0). st_hpd(order("I", "pizza", w), true, 1). st_hpd(put_down(w, "burnt pizza", t), true, 2). st_hpd(request("I", pick_up(w, "burnt pizza", t), w), true, 3).
```

---

## Story #17 — Partial Match (Similarity: 0.2727)

**Story:** 

### Predicted
```clingo
restaurant("the restaurant"). customer("he"). waiter("the waiter"). food("dinner"). st_hpd(put_down("the waiter", "dinner", t), true, 0). st_hpd(eat("he", "dinner"), true, 1). st_hpd(request("he", b, "the waiter"), true, 2). st_hpd(put_down("the waiter", b, t), false).
```

### Ground Truth
```clingo
customer("he"). food("something spotted with eggs and livers"). waiter("the waiter"). story_step(0..1). st_hpd(put_down("the waiter", "something spotted with eggs and livers", t), true, 0). st_hpd(eat("he", "something spotted with eggs and livers"), true, 1). st_hpd(put_down("the waiter", b, t), false).
```

---

## Story #18 — Partial Match (Similarity: 0.2778)

**Story:** 

### Predicted
```clingo
restaurant("meat restaurant"). customer("Herbie"). customer("his father"). waiter("the waiter"). food("steak"). food("haddock and creamed spinach"). food("lamb chops"). st_hpd(put_down("the waiter", "steak", t), true, 0). st_hpd(put_down("the waiter", "haddock and creamed spinach", t), true, 0). st_hpd(order_for("his father", "Herbie", "lamb chops", "the waiter"), true, 1).
```

### Ground Truth
```clingo
restaurant("a meat restaurant"). customer("Herbie"). customer("his father"). food("a sizzling steak"). food("haddock and creamed spinach"). food("lamb chops"). waiter("the waiter"). story_step(0..4). st_obs(in("Herbie", "a meat restaurant"), true, 0). st_obs(in("his father", "a meat restaurant"), true, 0). st_hpd(put_down("the waiter", "a sizzling steak", t), true, 1). st_hpd(put_down("the waiter", "haddock and creamed spinach", t), true, 2). st_hpd(request("his father", pick_up("the waiter", "haddock and creamed spinach", t), "the waiter"), true, 3). st_hpd(order_for("his father", "Herbie", "lamb chops", "the waiter"), true, 4).
```

---

## Story #34 — Partial Match (Similarity: 0.2857)

**Story:** 

### Predicted
```clingo
restaurant("RRGrill"). customer("Andy"). st_obs(open("RRGrill"), true, 0).
```

### Ground Truth
```clingo
restaurant("RRGrill"). customer("Andy"). story_step(0..2). st_hpd(enter("Andy", "RRGrill"), true, 0). st_obs(table_available, false, 1). st_hpd(wait("Andy"), true, 1). st_hpd(free_table, true, 2).
```

---

## Story #38 — Partial Match (Similarity: 0.2857)

**Story:** 

### Predicted
```clingo
restaurant("RRGrill"). customer("Andy"). waiter("the waiter"). st_obs(open("RRGrill"), true, 0). st_hpd(lead_to("the waiter", "Andy", t), true, 1). st_hpd(read_menu("Andy"), true, 2). st_hpd(order("Andy"), false). st_hpd(leave("Andy"), true, 3).
```

### Ground Truth
```clingo
restaurant("RRGrill"). customer("Andy"). food("nothing"). waiter("the waiter"). story_step(0..4). st_hpd(enter("Andy", "RRGrill"), true, 0). st_hpd(lead_to("the waiter", "Andy", t), true, 1). st_hpd(put_down("Andy", m, t), true, 2). st_stop_activity("Andy", 3). next_st(2, 3). st_hpd(leave("Andy"), true, 4).
```

---

## Story #43 — Partial Match (Similarity: 0.2941)

**Story:** 

### Predicted
```clingo
restaurant("the restaurant"). customer("Megan"). waiter("the bartender"). beverage("a glass of wine"). st_hpd(enter("Megan", "the restaurant"), true, 0). st_obs(at_l("Megan", "the bar"), true, 1). st_hpd(sit("Megan"), true, 1). st_hpd(order("Megan", "a glass of wine", "the bartender"), true, 2). st_hpd(put_down("the bartender", "a glass of wine", t), true, 3). st_hpd(drink("Megan", "a glass of wine"), true, 4). st_hpd(pay("Megan", b), true, 5). st_hpd(leave("Megan"), true, 6).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer("Megan"). beverage("glass of wine"). waiter("the bartender"). st_hpd(enter("Megan", "the restaurant"), true, 0). st_hpd(sit("Megan"), true, 1). st_hpd(order("Megan", "glass of wine", "the bartender"), true, 2). st_hpd(drink("Megan", "glass of wine"), true, 3). st_hpd(pay("Megan", b), true, 4). st_hpd(leave("Megan"), true, 5).
```

---

## Story #20 — Partial Match (Similarity: 0.3000)

**Story:** 

### Predicted
```clingo
restaurant("the restaurant"). customer("Molly"). customer("me"). waiter("the waiter"). food("escargot"). food(f). member("twelve oysters", f). member("twelve clams", f). beverage("wine"). st_hpd(put_down("the waiter", "escargot", t), true, 0). st_hpd(put_down("the waiter", f, t), true, 1). st_hpd(put_down("the waiter", "wine", t), true, 2).
```

### Ground Truth
```clingo
restaurant(r). customer(we). member("Molly", we). member(me, we). food(escargot). food(f). member("twelve oysters", f). member("twelve clams", f). beverage("wine"). waiter("the waiter"). story_step(0..3). st_hpd(put_down("the waiter", escargot, t), true, 0). st_hpd(put_down("the waiter", f, t), true, 1). st_hpd(eat(we, f), true, 2). st_hpd(put_down("the waiter", wine, t), true, 3).
```

---

## Story #2 — Partial Match (Similarity: 0.3333)

**Story:** 

### Predicted
```clingo
restaurant("the restaurant"). customer("John"). food("steak"). waiter("the waiter"). st_hpd(enter("John", "the restaurant"), true, 0). st_hpd(lead_to("the waiter", "John", t), true, 1). st_hpd(sit("John"), true, 2). st_hpd(order("John", "steak", "the waiter"), true, 3). st_hpd(put_down("the waiter", "steak", t), true, 4). st_hpd(request("John", b, "the waiter"), true, 5). st_hpd(put_down("the waiter", b, t), true, 6). st_hpd(pay("John", b), true, 7). st_hpd(leave("John"), true, 8).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer("John"). food("steak"). waiter("the waiter"). story_step(0..6). st_hpd(enter("John", "the restaurant"), true, 0). st_hpd(lead_to("the waiter", "John", t), true, 1). st_hpd(order("John", "steak", "the waiter"), true, 2). st_hpd(request("John", b, "the waiter"), true, 3). st_hpd(put_down("the waiter", b, t), true, 4). st_pay(pay("John", b), true, 5). st_pay(leave("John"), true, 6).
```

---

## Story #48 — Partial Match (Similarity: 0.3333)

**Story:** 

### Predicted
```clingo
restaurant("the restaurant"). customer("Olivia"). waiter("the waiter"). beverage("a glass of water"). st_hpd(sit("Olivia"), true, 0). st_hpd(greet("the waiter", "Olivia"), true, 1). st_hpd(order("Olivia", "a glass of water", "the waiter"), true, 2). st_hpd(put_down("the waiter", "a glass of water", t), true, 3).
```

### Ground Truth
```clingo
restaurant(r). customer("Olivia"). beverage("glass of water"). waiter("the waiter"). story_step(0..3). st_hpd(sit("Olivia"), true, 0). st_hpd(greet("the waiter", "Olivia"), true, 1). st_hpd(order("Olivia", "glass of water", "the waiter"), true, 2). st_hpd(put_down("the waiter", "glass of water", t), true, 3).
```

---

## Story #50 — Partial Match (Similarity: 0.3333)

**Story:** 

### Predicted
```clingo
restaurant("the restaurant"). customer("Fiona"). waiter("the waiter"). food("soup of the day"). food("a sandwich"). st_hpd(order("Fiona", "soup of the day", "the waiter"), true, 0). st_obs(available("soup of the day", "the restaurant"), false, 1). st_hpd(order("Fiona", "a sandwich", "the waiter"), true, 2).
```

### Ground Truth
```clingo
restaurant(r). customer("Fiona"). food("soup of the day"). food("sandwich"). waiter("the waiter"). story_step(0..2). st_hpd(order("Fiona", "soup of the day", "the waiter"), true, 0). st_obs(available("soup of the day", r), false, 1). st_hpd(order("Fiona", "sandwich", "the waiter"), true, 2).
```

---

## Story #53 — Partial Match (Similarity: 0.3333)

**Story:** 

### Predicted
```clingo
restaurant("family restaurant"). customer("Mr. Johnson"). customer("Mrs. Johnson"). customer("their son"). waiter("the waiter"). food("steak"). food("salad"). food("pizza"). st_hpd(enter("Mr. Johnson", "family restaurant"), true, 0). st_hpd(enter("Mrs. Johnson", "family restaurant"), true, 0). st_hpd(enter("their son", "family restaurant"), true, 0). st_obs(sitting("Mr. Johnson"), true, 1). st_obs(sitting("Mrs. Johnson"), true, 1). st_obs(sitting("their son"), true, 1). st_hpd(order("Mr. Johnson", "steak", "the waiter"), true, 2). st_hpd(order("Mrs. Johnson", "salad", "the waiter"), true, 2). st_hpd(order("their son", "pizza", "the waiter"), true, 2). st_hpd(put_down("the waiter", "steak", t), true, 3). st_hpd(put_down("the waiter", "salad", t), true, 3). st_hpd(put_down("the waiter", "pizza", t), true, 3).
```

### Ground Truth
```clingo
restaurant("family restaurant"). person("Mr. Johnson"). person("Mrs. Johnson"). person("son"). customer("Johnson family"). member("Mr. Johnson", "Johnson family"). member("Mrs. Johnson", "Johnson family"). member("son", "Johnson family"). food("steak"). food("salad"). food("pizza"). waiter("the waiter"). story_step(0..4). st_hpd(enter("Johnson family", "family restaurant"), true, 0). st_obs(sitting("Johnson family"), true, 1). st_hpd(order("Mr. Johnson", "steak", "the waiter"), true, 2). st_hpd(order("Mrs. Johnson", "salad", "the waiter"), true, 2). st_hpd(order("son", "pizza", "the waiter"), true, 2). st_hpd(put_down("the waiter", "steak", t), true, 3). st_hpd(put_down("the waiter", "salad", t), true, 3). st_hpd(put_down("the waiter", "pizza", t), true, 3).
```

---

## Story #66 — Partial Match (Similarity: 0.3333)

**Story:** 

### Predicted
```clingo
restaurant("the restaurant"). customer("Charlie"). waiter("the waiter"). food("a burger"). st_hpd(enter("Charlie", "the restaurant"), true, 0). st_hpd(lead_to("the waiter", "Charlie", t), true, 1). st_hpd(order("Charlie", "a burger", "the waiter"), true, 2). st_hpd(put_down("the waiter", "a burger", t), true, 3). st_hpd(eat("Charlie", "a burger"), true, 4). st_hpd(request("Charlie", b, "the waiter"), true, 5). st_hpd(pay("Charlie", b), true, 6). st_hpd(leave("Charlie"), true, 7).
```

### Ground Truth
```clingo
restaurant("a restaurant"). customer("Charlie"). food("burger"). waiter("the waiter"). story_step(0..7). st_hpd(enter("Charlie", "a restaurant"), true, 0). st_hpd(lead_to("the waiter", "Charlie", t), true, 1). st_hpd(order("Charlie", "burger", "the waiter"), true, 2). st_hpd(put_down("the waiter", "burger", t), true, 3). st_hpd(eat("Charlie", "burger"), true, 4). st_hpd(request("Charlie", b, "the waiter"), true, 5). st_hpd(pay("Charlie", b), true, 6). st_hpd(leave("Charlie"), true, 7).
```

---

## Story #65 — Partial Match (Similarity: 0.3478)

**Story:** 

### Predicted
```clingo
restaurant("Italian restaurant"). customer("Maria"). waiter("the waiter"). host("the host"). food("spaghetti carbonara"). beverage("a glass of red wine"). st_hpd(enter("Maria", "Italian restaurant"), true, 0). st_hpd(greet("the host", "Maria"), true, 1). st_hpd(lead_to("the host", "Maria", t), true, 2). st_hpd(read_menu("Maria"), true, 3). st_hpd(order("Maria", "spaghetti carbonara", "the waiter"), true, 4). st_hpd(order("Maria", "a glass of red wine", "the waiter"), true, 4). st_hpd(put_down("the waiter", "spaghetti carbonara", t), true, 5). st_hpd(put_down("the waiter", "a glass of red wine", t), true, 5). st_hpd(request("Maria", b, "the waiter"), true, 6).
```

### Ground Truth
```clingo
restaurant("Italian restaurant"). customer("Maria"). person("the host"). food("spaghetti carbonara"). beverage("red wine"). waiter("the waiter"). story_step(0..6). st_hpd(enter("Maria", "Italian restaurant"), true, 0). st_hpd(greet("the host", "Maria"), true, 1). st_hpd(lead_to("the host", "Maria", t), true, 2). st_hpd(order("Maria", "spaghetti carbonara", "the waiter"), true, 3). st_hpd(order("Maria", "red wine", "the waiter"), true, 3). st_hpd(put_down("the waiter", "spaghetti carbonara", t), true, 4). st_hpd(put_down("the waiter", "red wine", t), true, 4). st_hpd(eat("Maria", "spaghetti carbonara"), true, 5). st_hpd(drink("Maria", "red wine"), true, 5). st_hpd(request("Maria", b, "the waiter"), true, 6).
```

---

## Story #10 — Partial Match (Similarity: 0.3636)

**Story:** 

### Predicted
```clingo
restaurant("the restaurant"). customer("Jim"). food("an appetizer"). waiter("the waiter"). st_obs(sitting("Jim"), true, 0). st_hpd(order("Jim", "an appetizer", "the waiter"), true, 1). st_obs(served("Jim"), false, 2). st_hpd(leave("Jim"), true, 3).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer("Jim"). food("appetizer"). story_step(0..3). st_obs(sitting("Jim"), true, 0). st_hpd(order("Jim", "appetizer", w), true, 1). st_obs(served("Pete"), false, 2). st_hpd(leave("Jim"), true, 3).
```

---

## Story #37 — Partial Match (Similarity: 0.3750)

**Story:** 

### Predicted
```clingo
restaurant("RRGrill"). restaurant("Happy Pizza"). customer("Andy"). st_obs(open("RRGrill"), false, 0). st_hpd(enter("Andy", "Happy Pizza"), true, 1).
```

### Ground Truth
```clingo
restaurant("RRGrill"). restaurant("Happy Pizza"). customer("Andy"). story_step(0..2). st_obs(closed("RRGrill"), true, 0). stop_activity("Andy", 1). st_hpd(move("Andy", "RRGrill", "Happy Pizza"), true, 2).
```

---

## Story #41 — Partial Match (Similarity: 0.3750)

**Story:** 

### Predicted
```clingo
restaurant("cafe"). customer("Laura"). waiter("the waiter"). beverage("coffee"). food("a croissant"). st_obs(in("Laura", "cafe"), true, 0). st_hpd(order("Laura", "coffee", "the waiter"), true, 1). st_hpd(order("Laura", "a croissant", "the waiter"), true, 1). st_hpd(put_down("the waiter", "coffee", t), true, 2). st_hpd(pay("Laura", b), true, 3). st_hpd(leave("Laura"), true, 4).
```

### Ground Truth
```clingo
restaurant("cafe"). customer("Laura"). beverage("coffee"). food("croissant").  waiter("the waiter"). story_step(0..4). st_hpd(order("Laura", "coffee", "the waiter"), true, 0). st_hpd(order("Laura", "croissant", "the waiter"), true, 0). st_hpd(put_down("the waiter", "coffee", t), true, 1). st_obs(served("Laura"), false, 2). st_hpd(pay("Laura", b), true, 3). st_hpd(leave("Laura"), true, 4).
```

---

## Story #3 — Partial Match (Similarity: 0.4000)

**Story:** 

### Predicted
```clingo
restaurant("the restaurant"). customer("Jill"). food("chicken"). waiter("the waiter"). st_hpd(enter("Jill", "the restaurant"), true, 0). st_hpd(lead_to("the waiter", "Jill", t), true, 1). st_hpd(sit("Jill"), true, 2). st_hpd(order("Jill", "chicken", "the waiter"), true, 3). st_hpd(put_down("the waiter", "chicken", t), true, 4). st_hpd(eat("Jill", "chicken"), true, 5). st_hpd(request("Jill", b, "the waiter"), true, 6).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer("Jill"). food("chicken"). waiter("the waiter"). story_step(0..5). st_hpd(enter("Jill", "the restaurant"), true, 0). st_hpd(lead_to("the waiter", "Jill", t), true, 1). st_hpd(order("Jill", "chicken", "the waiter"), true, 2). st_hpd(put_down("the waiter", "chicken", t), true, 3). st_hpd(eat("Jill", "chicken"), true, 4). st_hpd(request("Jill", b, "the waiter"), true, 5).
```

---

## Story #25 — Partial Match (Similarity: 0.4000)

**Story:** 

### Predicted
```clingo
restaurant("the restaurant"). customer("I"). waiter("the head-waiter"). customer("Uncle Chipperton"). food("dinner"). st_hpd(enter("I", "the restaurant"), true, 0). st_hpd(sit("I"), true, 1). st_hpd(put_down("the head-waiter", "dinner", t), true, 2). st_hpd(eat("I", "dinner"), true, 3). st_hpd(enter("Uncle Chipperton", "the restaurant"), true, 4). st_hpd(pay("Uncle Chipperton", b), true, 5).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer("I"). waiter("head-waiter") food("capital dinner"). person("Uncle Chipperton"). story_step(0..5). st_hpd(enter("I", "the restaurant"), true, 0). st_hpd(sit("I"), true, 1). st_hpd(put_down("head-waiter", "capital dinner", t), true, 2). st_hpd(eat("I", "capital dinner"), true, 3). st_hpd(enter("Uncle Chipperton", "the restaurant"), true, 4). st_hpd(pay("Uncle Chipperton", b), true, 5).
```

---

## Story #33 — Partial Match (Similarity: 0.4000)

**Story:** 

### Predicted
```clingo
restaurant("RRGrill"). customer("Andy"). st_obs(open("RRGrill"), true, 0).
```

### Ground Truth
```clingo
restaurant("RRGrill"). customer("Andy"). story_step(0..1). st_hpd(enter("Andy", "RRGrill"), true, 0). st_obs(table_available, false, 1).
```

---

## Story #9 — Partial Match (Similarity: 0.4375)

**Story:** 

### Predicted
```clingo
restaurant("the restaurant"). customer("Pete"). food("chicken"). waiter("the waiter"). st_obs(sitting("Pete"), true, 0). st_hpd(order("Pete", "chicken", "the waiter"), true, 1). st_hpd(put_down("the waiter", "chicken", t), true, 2). st_hpd(complain("Pete", "the waiter"), true, 3). st_next(2,3). food("a better cooked dish"). st_hpd(request("Pete", "a better cooked dish", "the waiter"), true, 4).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer("Pete"). food("chicken"). food("undercooked chicken"). food("better cooked chicken"). waiter("the waiter"). story_step(0..4). st_obs(sitting("Pete"), true, 0). st_hpd(order("Pete", "chicken", "the waiter"), true, 1). st_hpd(put_down("the waiter", "undercooked_chicken", t), true, 2). st_hpd(complain("Pete", "the waiter"), true, 3). st_next(2, 3). st_hpd(order("Pete", "better cooked chicken", "the waiter"), true, 4).
```

---

## Story #7 — Partial Match (Similarity: 0.4444)

**Story:** 

### Predicted
```clingo
restaurant("the restaurant"). customer("Larry"). waiter("the waiter"). st_obs(sitting("Larry"), true, 0). st_hpd(read_menu("Larry"), true, 1). st_hpd(order("Larry"), false).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer("Larry"). waiter("the waiter"). story_step(0..3). st_obs(sitting("Larry"), true, 0). st_hpd(put_down("the waiter", m, t), true, 1). st_obs(menu_read("Larry"), true, 2). st_hpd(order("Larry"), false, 3).
```

---

## Story #8 — Partial Match (Similarity: 0.4545)

**Story:** 

### Predicted
```clingo
restaurant("the restaurant"). customer("Derek"). food("vegetable soup"). waiter("the waiter"). st_hpd(order("Derek", "vegetable soup", "the waiter"), true, 0). st_hpd(put_down("the waiter", "vegetable soup", t), true, 1). st_hpd(cancel_bill("the waiter"), true, 2).
```

### Ground Truth
```clingo
restaurant("restaurant"). customer("Derek"). food("vegetable soup"). waiter("the waiter"). story_step(0..3). st_hpd(order("Derek", "vegetable soup", "the waiter"), true, 0). st_hpd(put_down("the waiter", "vegetable soup", t), true, 1). st_hpd(complain("Derek", "the waiter"), true, 2). st_next(1, 2). st_hpd(pay("derek", b), false, 3).
```

---

## Story #39 — Partial Match (Similarity: 0.4545)

**Story:** 

### Predicted
```clingo
restaurant("RRGrill"). customer("Andy"). waiter("the waiter"). st_obs(open("RRGrill"), true, 0). st_hpd(lead_to("the waiter", "Andy", t), true, 1). st_hpd(sit("Andy"), true, 2). st_hpd(order("Andy"), false). st_hpd(leave("Andy"), true, 3).
```

### Ground Truth
```clingo
restaurant("RRGrill"). customer("Andy"). waiter("the waiter"). story_step(0..3). st_hpd(enter("Andy", "RRGrill"), true, 0). st_hpd(lead_to("the waiter", "Andy", t), true, 1). st_obs(sitting("Andy"), true, 2). st_stop_activity("Andy", 2). st_hpd(leave("Andy"), true, 3).
```

---

## Story #73 — Partial Match (Similarity: 0.5333)

**Story:** 

### Predicted
```clingo
restaurant("the deli"). customer("David"). waiter("the server"). food(f). member("a pastrami sandwich", f). member("a pickle", f). st_hpd(enter("David", "the deli"), true, 0). st_obs(at_l("David", "the counter"), true, 1). st_hpd(order("David", f, "the server"), true, 2). st_hpd(prepare("the cook", f, "the server"), true, 3). st_hpd(put_down("the server", f, t), true, 4). st_hpd(eat("David", f), true, 5).
```

### Ground Truth
```clingo
restaurant("the deli"). customer("David"). food(f). member("pastrami sandwich", f). member("pickle", f). st_hpd(enter("David", "the deli"), true, 0). st_hpd(sit("David"), true, 1). st_hpd(order("David", f, "the server"), true, 2). st_hpd(prepare("the cook", f, "the server"), true, 3). st_hpd(put_down("the server", f, t), true, 4). st_hpd(eat("David", f), true, 5).
```

---

## Story #62 — Partial Match (Similarity: 0.5455)

**Story:** 

### Predicted
```clingo
restaurant("steakhouse"). customer("Wendy"). waiter("the waiter"). food("well-done steak"). food("rare steak"). st_hpd(order("Wendy", "well-done steak", "the waiter"), true, 0). st_hpd(put_down("the waiter", "rare steak", t), true, 1). st_hpd(pick_up("the waiter", "rare steak", t), true, 2).
```

### Ground Truth
```clingo
restaurant("the steakhouse"). customer("Wendy"). food("rare steak"). food("well-done steak"). waiter("the waiter"). story_step(0..2). st_hpd(order("Wendy", "well-done steak", "the waiter"), true, 0). st_hpd(put_down("the waiter", "rare steak", t), true, 1). st_hpd(request("Wendy", pick_up("the waiter", "rare steak", t), "the waiter"), true, 2). st_next(1, 2).
```

---

## Story #40 — Partial Match (Similarity: 0.5833)

**Story:** 

### Predicted
```clingo
restaurant("sushi restaurant"). customer("Ken"). waiter("the waiter"). food("tuna roll"). st_hpd(order("Ken", "tuna roll", "the waiter"), true, 0). st_hpd(put_down("the waiter", "tuna roll", t), true, 1). st_hpd(complain("Ken", "the waiter"), true, 2). st_next(1,2). st_hpd(put_down("the waiter", "hair-free tuna roll", t), true, 3).
```

### Ground Truth
```clingo
restaurant("sushi restaurant"). customer("Ken"). food("tuna roll"). food("new tuna roll"). waiter("the waiter"). story_step(0..4). st_hpd(order("Ken", "tuna roll", "the waiter"), true, 0). st_hpd(put_down("the waiter", "tuna roll", t), true, 1). st_hpd(complain("Ken", "the waiter"), true, 2). st_next(1, 2). st_hpd(put_down(w, "new tuna roll", t), true, 3).
```

---

## Story #11 — Partial Match (Similarity: 0.6000)

**Story:** 

### Predicted
```clingo
restaurant("the restaurant"). customer("Jake"). food("medium-rare steak"). food("rare steak"). waiter("the waiter"). st_obs(sitting("Jake"), true, 0). st_hpd(order("Jake", "medium-rare steak", "the waiter"), true, 1). st_hpd(put_down("the waiter", "rare steak", t), true, 2).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer("Jake"). food("medium-rare steak"). food("too rare steak"). waiter("the waiter"). story_step(0..2). st_obs(sitting("Jake"), true, 0). st_hpd(order("Jake", "medium-rare steak", "the waiter"), true, 1). st_hpd(put_down("the waiter", "too rare steak", t), true, 2).
```

---

## Story #16 — Partial Match (Similarity: 0.6667)

**Story:** 

### Predicted
```clingo
restaurant("the restaurant"). customer("Gavin"). customer("Amandine"). waiter("the waiter"). st_hpd(lead_to("the waiter", "Gavin", t), true, 0). st_hpd(lead_to("the waiter", "Amandine", t), true, 0). st_hpd(sit("Gavin"), true, 1). st_hpd(sit("Amandine"), true, 1). st_hpd(read_menu("Gavin"), true, 2). food(f). member("egg drop soup with wonton", f). member("lobster Cantonese and shrimp", f). member("beef and pork fried rice", f). st_hpd(order("Amandine", f, "the waiter"), true, 3). st_hpd(order("Gavin", f, "the waiter"), true, 4).
```

### Ground Truth
```clingo
waiter("the waiter"). customer("Gavin"). customer("Amandine"). food(f). member("egg drop soup with wonton", f). member("lobster Cantonese", f). member("shrimp, beef and pork fried rice", f). story_step(0..4). st_hpd(lead_to("the waiter", "Gavin", t), true, 0). st_hpd(lead_to("the waiter", "Amandine", t), true, 0). st_hpd(sit("Gavin"), true, 1). st_hpd(sit("Amandine"), true, 1). st_hpd(read_menu("Gavin"), true, 2). st_hpd(read_menu("Amandine"), false). st_hpd(order("Amandine", f, "the waiter"), true, 3). st_hpd(order("Gavin", f, "the waiter"), true, 4).
```

---

## Story #52 — Partial Match (Similarity: 0.6923)

**Story:** 

### Predicted
```clingo
restaurant("seafood restaurant"). customer("David"). waiter("the waiter"). food("grilled salmon with vegetables"). st_hpd(enter("David", "seafood restaurant"), true, 0). st_hpd(lead_to("the waiter", "David", t), true, 1). st_hpd(read_menu("David"), true, 2). st_hpd(order("David", "grilled salmon with vegetables", "the waiter"), true, 3). st_hpd(eat("David", "grilled salmon with vegetables"), true, 4). st_hpd(pay("David", b), true, 5). st_hpd(leave("David"), true, 6).
```

### Ground Truth
```clingo
restaurant("seafood restaurant"). customer("David"). food("grilled salmon with vegetables"). waiter("the waiter"). st_hpd(enter("David", "seafood restaurant"), true, 0). st_hpd(lead_to("the waiter", "David", t), true, 1). st_hpd(order("David", "grilled salmon with vegetables", "the waiter"), true, 2). st_hpd(put_down("the waiter", "grilled salmon with vegetables", t), true, 3). st_hpd(eat("David", "grilled salmon with vegetables"), true, 4). st_hpd(pay("David", b), true, 5). st_hpd(leave("David"), true, 6).
```

---

## Story #44 — Partial Match (Similarity: 0.7000)

**Story:** 

### Predicted
```clingo
restaurant("Italian restaurant"). customer("Chloe"). waiter("the waiter"). food("lasagna"). food("spaghetti"). st_hpd(order("Chloe", "lasagna", "the waiter"), true, 0). st_hpd(put_down("the waiter", "spaghetti", t), true, 1). st_obs(informed("Chloe", "wrong dish", "the waiter"), true, 2).
```

### Ground Truth
```clingo
restaurant("Italian restaurant"). customer("Chloe"). food("lasagna"). food("spaghetti"). waiter("the waiter"). story_step(0..2). st_hpd(order("Chloe", "lasagna", "the waiter"), true, 0). st_hpd(put_down("the waiter", "spaghetti", t), true, 1). st_hpd(complain("Chloe", "the waiter"), true, 2). st_next(1, 2).
```

---

## Story #46 — Partial Match (Similarity: 0.7778)

**Story:** 

### Predicted
```clingo
restaurant("the restaurant"). customer("Rita"). waiter("the waiter"). food("salad"). st_hpd(eat("Rita", "salad"), true, 0). st_hpd(request("Rita", b, "the waiter"), true, 1). st_hpd(put_down("the waiter", b, t), true, 2). st_hpd(pay("Rita", b), true, 3).
```

### Ground Truth
```clingo
restaurant(r). customer("Rita"). food("salad"). waiter("the waiter"). story_step(0..3). st_hpd(eat("Rita", "salad"), true, 0). st_hpd(request("Rita", b, "the waiter"), true, 1). st_hpd(put_down("the waiter", b, t), true, 2). st_hpd(pay("Rita", b), true, 3).
```

---

## Story #60 — Partial Match (Similarity: 0.8182)

**Story:** 

### Predicted
```clingo
restaurant("the restaurant"). customer("Robert"). waiter("the waiter"). food("medium-rare steak"). food("well-done steak"). st_hpd(order("Robert", "medium-rare steak", "the waiter"), true, 0). st_hpd(put_down("the waiter", "well-done steak", t), true, 1). st_hpd(complain("Robert", "the waiter"), true, 2). st_next(1,2). st_hpd(pick_up("the waiter", "well-done steak", t), true, 3).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer("Robert"). food("medium-rare steak"). food("well-done steak"). waiter("the waiter"). story_step(0..3). st_hpd(order("Robert", "medium-rare steak", "the waiter"), true, 0). st_hpd(put_down("the waiter", "well-done steak", t), true, 1). st_hpd(complain("Robert", "the waiter"), true, 2). st_next(1, 2). st_hpd(pick_up("the waiter", "well-done steak", t), true, 3).
```

---

## Story #68 — Partial Match (Similarity: 0.8462)

**Story:** 

### Predicted
```clingo
restaurant("local diner"). customer("Frank"). waiter("the waitress"). beverage("black coffee"). food("pancakes"). st_hpd(sit("Frank"), true, 0). st_hpd(put_down("the waitress", "black coffee", t), true, 1). st_hpd(read_menu("Frank"), true, 2). st_hpd(order("Frank", "pancakes", "the waitress"), true, 3). st_hpd(eat("Frank", "pancakes"), true, 4). st_hpd(pay("Frank", b), true, 5). st_hpd(leave("Frank"), true, 6).
```

### Ground Truth
```clingo
restaurant("local diner"). customer("Frank"). beverage("black coffee"). food("pancakes"). waiter("the waitress"). story_step(0..6). st_obs(sitting("Frank"), true, 0). st_hpd(put_down("the waitress", "black coffee", t), true, 1). st_hpd(read_menu("Frank"), true, 2). st_hpd(order("Frank", "pancakes", "the waitress"), true, 3). st_hpd(eat("Frank", "pancakes"), true, 4). st_hpd(pay("Frank", b), true, 5). st_hpd(leave("Frank"), true, 6).
```

---

## Story #0 — Partial Match (Similarity: 1.0000)

**Story:** 

### Predicted
```clingo
restaurant("the restaurant"). customer("Allie"). food("fruit salad"). waiter("the waiter"). st_hpd(enter("Allie", "the restaurant"), true, 0). st_hpd(lead_to("the waiter", "Allie", t), true, 1). st_hpd(sit("Allie"), true, 2). st_hpd(order("Allie", "fruit salad", "the waiter"), true, 3). st_hpd(put_down("the waiter", "fruit salad", t), true, 4). st_hpd(eat("Allie", "fruit salad"), true, 5). st_hpd(request("Allie", b, "the waiter"), true, 6).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer("Allie"). food("fruit salad"). waiter("the waiter"). story_step(0..6). st_hpd(enter("Allie", "the restaurant"), true, 0). st_hpd(lead_to("the waiter", "Allie", t), true, 1). st_hpd(sit("Allie"), true, 2). st_hpd(order("Allie", "fruit salad", "the waiter"), true, 3). st_hpd(put_down("the waiter", "fruit salad", t), true, 4). st_hpd(eat("Allie", "fruit salad"), true, 5). st_hpd(request("Allie", b, "the waiter"), true, 6).
```

---

## Story #4 — Partial Match (Similarity: 1.0000)

**Story:** 

### Predicted
```clingo
restaurant("the restaurant"). customer("Bob"). food("hamburger"). waiter("the waiter"). st_obs(sitting("Bob"), true, 0). st_hpd(order("Bob", "hamburger", "the waiter"), true, 1).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer("Bob"). food("hamburger"). waiter("the waiter"). story_step(0..1). st_obs(sitting("Bob"), true, 0). st_hpd(order("Bob", "hamburger", "the waiter"), true, 1).
```

---

## Story #5 — Partial Match (Similarity: 1.0000)

**Story:** 

### Predicted
```clingo
restaurant("the restaurant"). customer("Jane"). food("fish"). waiter("the waiter"). st_hpd(lead_to("the waiter", "Jane", t), true, 0). st_obs(sitting("Jane"), true, 1). st_hpd(order("Jane", "fish", "the waiter"), true, 2). st_hpd(eat("Jane", "fish"), true, 3). st_hpd(put_down("the waiter", b, t), true, 4).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer("Jane"). food("fish"). waiter("the waiter"). story_step(0..4). st_hpd(lead_to("the waiter", "Jane", t), true, 0). st_obs(sitting("Jane"), true, 1). st_hpd(order("Jane", "fish", "the waiter"), true, 2). st_hpd(eat("Jane", "fish"), true, 3). st_hpd(put_down("the waiter", b, t), true, 4).
```

---

## Story #6 — Partial Match (Similarity: 1.0000)

**Story:** 

### Predicted
```clingo
restaurant("the restaurant"). customer("Molly"). food("baked potato"). food("French fries"). waiter("the waiter"). st_obs(sitting("Molly"), true, 0). st_hpd(order("Molly", "baked potato", "the waiter"), true, 1). st_hpd(put_down("the waiter", "French fries", t), true, 2).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer("Molly"). food("baked potato"). food("French fries"). waiter("the waiter"). story_step(0..2). st_obs(sitting("Molly"), true, 0). st_hpd(order("Molly", "baked potato", "the waiter"), true, 1). st_hpd(put_down("the waiter", "French fries", t), true, 2).
```

---

## Story #63 — Partial Match (Similarity: 1.0000)

**Story:** 

### Predicted
```clingo
restaurant("cafe"). customer("Ivan"). waiter("the waiter"). beverage("espresso"). st_hpd(order("Ivan", "espresso", "the waiter"), true, 0). st_hpd(put_down("the waiter", "espresso", t), true, 1). st_hpd(drink("Ivan", "espresso"), true, 2). st_hpd(pay("Ivan", b), true, 3). st_hpd(leave("Ivan"), true, 4).
```

### Ground Truth
```clingo
restaurant("cafe"). customer("Ivan"). beverage("espresso"). waiter("the waiter"). story_step(0..4). st_hpd(order("Ivan", "espresso", "the waiter"), true, 0). st_hpd(put_down("the waiter", "espresso", t), true, 1). st_hpd(drink("Ivan", "espresso"), true, 2). st_hpd(pay("Ivan", b), true, 3). st_hpd(leave("Ivan"), true, 4).
```

---
