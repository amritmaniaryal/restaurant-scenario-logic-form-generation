# DeepSeek_evaluated

## Summary

- Total common: 100
- Exact matches: 1
- Partial matches: 99
- Accuracy: 0.01

---

## Story #98 — Exact Match (Similarity: 1.0000)

**Story:** [REDACTED — original ROCStories text; storyid=09a69527-2433-4e12-9943-9dcacbdf9b04]

### Predicted
```clingo
restaurant("new place"). customer("Joe"). person("Joe"). food("meal"). st_obs(hungry("Joe"), true, 0). st_hpd(enter("Joe", "new place"), true, 1). st_hpd(order("Joe", "meal", w), true, 2). st_hpd(eat("Joe", "meal"), true, 3). st_obs(hungry("Joe"), false, 4).
```

### Ground Truth
```clingo
restaurant("new place"). customer("Joe"). food("a meal"). st_obs(hungry("Joe"), true, 0). st_hpd(enter("Joe", "new place"), true, 1). st_hpd(order("Joe", "a meal", w), true, 2). st_hpd(eat("Joe", "a meal"), true, 3). st_obs(hungry("Joe"), false, 4).
```

---

## Story #24 — Partial Match (Similarity: 0.0000)

**Story:** Jasper invited Frank to a restaurant. Jasper ordered roast beef and coffee. Their conversation was interrupted by the arrival of the coffee and roast beef, which both he and his new friend attacked with vigor. Jasper wanted to invite Frank, but he had forgotten his wallet at home. Frank paid for both.

### Predicted
```clingo
restaurant(r). customer("Jasper"). customer("Frank"). person("Jasper"). person("Frank"). food("roast beef"). beverage("coffee"). st_hpd(invite("Jasper", "Frank", r), true, 0). st_hpd(order("Jasper", "roast beef", w), true, 1). st_hpd(order("Jasper", "coffee", w), true, 1). st_hpd(bring(w, "coffee", "table"), true, 2). st_hpd(bring(w, "roast beef", "table"), true, 2). st_hpd(eat("Jasper", "roast beef"), true, 3). st_hpd(eat("Frank", "roast beef"), true, 3). st_hpd(drink("Jasper", "coffee"), true, 4). st_hpd(drink("Frank", "coffee"), true, 4). st_hpd(pay("Frank", b), true, 5).
```

### Ground Truth
```clingo
restaurant("a restaurant"). customer(they). member("Jasper", they). member("Frank", they). food(f). member("roast beef", f). member(coffee, f). waiter(w). story_step(0..4). st_hpd(enter(they, "a restaurant"), true, 0). st_hpd(order_for("Jasper", they, f, w), true, 1). st_hpd(put_down(w, f, t), true, 2). st_hpd(eat(they, f), true, 3). st_hpd(pay("Jasper", b), false, 4). st_hpd(pay("Frank", b), true, 4).
```

---

## Story #19 — Partial Match (Similarity: 0.0392)

**Story:** Brand sat in a chair. He picked up the menu and ordered a whiskey with Pepsi, but no ice. Pyrogies and sausage cooked in sauerkraut, he told the waiter. The waiter brought Brand his drink. Then, the waiter placed the food on the table. Brand asked the waiter to bring him a large bowl of borscht when he was done with the pyrogies and sausage. The waiter went back into the kitchen. Brand ate the pyrogies and then the sausage and sauerkraut. Then, the waiter brought out Brand's bowl of soup.

### Predicted
```clingo
restaurant("the restaurant"). customer("Brand"). person("Brand"). beverage("whiskey with Pepsi, but no ice"). food("Pyrogies"). food("sausage cooked in sauerkraut"). food("large bowl of borscht"). waiter("the waiter"). st_obs(sitting("Brand"), true, 0). st_obs(at_l("Brand", t), true, 0). st_obs(in("Brand", "the restaurant"), true, 0). st_hpd(pick_up("Brand", "the menu", t), true, 1). st_hpd(order("Brand", "whiskey with Pepsi, but no ice", "the waiter"), true, 2). st_hpd(order("Brand", "Pyrogies", "the waiter"), true, 2). st_hpd(order("Brand", "sausage cooked in sauerkraut", "the waiter"), true, 2). st_hpd(prepare("the cook", "whiskey with Pepsi, but no ice", "the waiter"), true, 3). st_hpd(move("the waiter", "the kitchen", t), true, 4). st_obs(holding("the waiter", "whiskey with Pepsi, but no ice"), true, 4). st_hpd(put_down("the waiter", "whiskey with Pepsi, but no ice", t), true, 5). st_hpd(drink("Brand", "whiskey with Pepsi, but no ice"), true, 6). st_hpd(prepare("the cook", "Pyrogies", "the waiter"), true, 7). st_hpd(prepare("the cook", "sausage cooked in sauerkraut", "the waiter"), true, 7). st_hpd(move("the waiter", "the kitchen", t), true, 8). st_obs(holding("the waiter", "Pyrogies"), true, 8). st_obs(holding("the waiter", "sausage cooked in sauerkraut"), true, 8). st_hpd(put_down("the waiter", "Pyrogies", t), true, 9). st_hpd(put_down("the waiter", "sausage cooked in sauerkraut", t), true, 9). st_hpd(request("Brand", "large bowl of borscht", "the waiter"), true, 10). st_hpd(move("the waiter", "the kitchen", t), true, 11). st_hpd(eat("Brand", "Pyrogies"), true, 12). st_hpd(eat("Brand", "sausage cooked in sauerkraut"), true, 13). st_hpd(prepare("the cook", "large bowl of borscht", "the waiter"), true, 14). st_hpd(move("the waiter", "the kitchen", t), true, 15). st_obs(holding("the waiter", "large bowl of borscht"), true, 15). st_hpd(put_down("the waiter", "large bowl of borscht", t), true, 16). st_hpd(eat("Brand", "large bowl of borscht"), true, 17).
```

### Ground Truth
```clingo
restaurant(r). customer("Brand"). beverage("whiskey with Pepsi, no ice"). food(f). member(pyrogies, f). member("sausage in sauerkraut", f). food(borscht). waiter("the waiter"). story_step(0..9). st_hpd(sit("Brand"), true, 0). st_hpd(pick_up("Brand", m, t), true, 1). st_hpd(order("Brand", "whiskey with Pepsi, no ice", "the waiter"), true, 2). st_hpd(order("Brand", f, "the waiter"), true, 3). st_hpd(put_down("the waiter", "whiskey with Pepsi, no ice"), t), true, 4). st_hpd(put_down("the waiter", f, t), true, 5). st_hpd(order("Brand", borscht, "the waiter"), true, 6). st_hpd(move("the waiter", t, kitchen), true, 7). st_hpd(eat("Brand", f), true, 8). st_hpd(put_down("the waiter", borscht, t), true, 9).
```

---

## Story #12 — Partial Match (Similarity: 0.0698)

**Story:** My husband and I went to a famous restaurant listed in our guidebook. We were seated at a booth and began studying the menu. We ordered escargot, lamb, savory salmon, and a creamy flan dessert.

### Predicted
```clingo
restaurant("a famous restaurant"). customer("My husband"). customer("I"). person("My husband"). person("I"). food("escargot"). food("lamb"). food("savory salmon"). food("creamy flan dessert"). waiter("the waiter"). st_hpd(enter("My husband", "a famous restaurant"), true, 0). st_hpd(enter("I", "a famous restaurant"), true, 0). st_obs(in("My husband", "a famous restaurant"), true, 0). st_obs(in("I", "a famous restaurant"), true, 0). st_hpd(sit("My husband"), true, 1). st_hpd(sit("I"), true, 1). st_obs(sitting("My husband"), true, 1). st_obs(sitting("I"), true, 1). st_obs(at_l("My husband", t), true, 1). st_obs(at_l("I", t), true, 1). st_hpd(pick_up("My husband", "the menu", t), true, 2). st_hpd(pick_up("I", "the menu", t), true, 2). st_hpd(read_menu("My husband"), true, 3). st_hpd(read_menu("I"), true, 3). st_obs(menu_read("My husband"), true, 3). st_obs(menu_read("I"), true, 3). st_hpd(order("My husband", "escargot", "the waiter"), true, 4). st_hpd(order("My husband", "lamb", "the waiter"), true, 4). st_hpd(order("My husband", "savory salmon", "the waiter"), true, 4). st_hpd(order("My husband", "creamy flan dessert", "the waiter"), true, 4). st_hpd(order("I", "escargot", "the waiter"), true, 4). st_hpd(order("I", "lamb", "the waiter"), true, 4). st_hpd(order("I", "savory salmon", "the waiter"), true, 4). st_hpd(order("I", "creamy flan dessert", "the waiter"), true, 4).
```

### Ground Truth
```clingo
restaurant("a famous restaurant"). person("my husband"). person("I"). customer("we"). member("my husband", "we"). member("I", "we"). member("escargot", f). member("lamb", f). member("savory salmon", f). member("creamy flan dessert", f) story_step(0..3). st_hpd(enter("we", "a famous restaurant"), true, 0). st_obs(sitting("we"), true, 1). st_hpd(read_menu("we"), true, 2). st_hpd(order("we", f, w), true, 3).
```

---

## Story #34 — Partial Match (Similarity: 0.0714)

**Story:** One day, Andy felt hungry and went to the RRGrill restaurant for dinner. The restaurant was open, but there was no table available for Andy. Andy decided to wait. A table became available soon after.

### Predicted
```clingo
restaurant("RRGrill restaurant"). customer("Andy"). person("Andy"). st_obs(hungry("Andy"), true, 0). st_obs(open("RRGrill restaurant"), true, 1). st_obs(at_l(t, "RRGrill restaurant"), false, 1). st_hpd(enter("Andy", "RRGrill restaurant"), true, 2). st_obs(in("Andy", "RRGrill restaurant"), true, 2). st_hpd(wait("Andy"), true, 3). st_obs(at_l(t, "RRGrill restaurant"), true, 4).
```

### Ground Truth
```clingo
restaurant("RRGrill"). customer("Andy"). story_step(0..2). st_hpd(enter("Andy", "RRGrill"), true, 0). st_obs(table_available, false, 1). st_hpd(wait("Andy"), true, 1). st_hpd(free_table, true, 2).
```

---

## Story #16 — Partial Match (Similarity: 0.0750)

**Story:** The waiter took Gavin and Amandine to a booth. They slid onto brown vinyl seats. Gavin glanced over his menu. Amandine didn't need to look to know what she wanted. She ordered egg drop soup with wonton, lobster Cantonese and shrimp, beef and pork fried rice. Gavin ordered the same.

### Predicted
```clingo
restaurant("the restaurant"). customer("Gavin"). customer("Amandine"). person("Gavin"). person("Amandine"). food("egg drop soup with wonton"). food("lobster Cantonese and shrimp"). food("beef and pork fried rice"). waiter("the waiter"). st_hpd(enter("Gavin", "the restaurant"), true, 0). st_hpd(enter("Amandine", "the restaurant"), true, 0). st_obs(in("Gavin", "the restaurant"), true, 0). st_obs(in("Amandine", "the restaurant"), true, 0). st_hpd(lead_to("the waiter", "Gavin", t), true, 1). st_hpd(lead_to("the waiter", "Amandine", t), true, 1). st_hpd(sit("Gavin"), true, 2). st_hpd(sit("Amandine"), true, 2). st_obs(sitting("Gavin"), true, 2). st_obs(sitting("Amandine"), true, 2). st_obs(at_l("Gavin", t), true, 2). st_obs(at_l("Amandine", t), true, 2). st_hpd(pick_up("Gavin", "the menu", t), true, 3). st_hpd(read_menu("Gavin"), true, 4). st_obs(menu_read("Gavin"), true, 4). st_hpd(order("Amandine", "egg drop soup with wonton", "the waiter"), true, 5). st_hpd(order("Amandine", "lobster Cantonese and shrimp", "the waiter"), true, 5). st_hpd(order("Amandine", "beef and pork fried rice", "the waiter"), true, 5). st_hpd(order("Gavin", "egg drop soup with wonton", "the waiter"), true, 5). st_hpd(order("Gavin", "lobster Cantonese and shrimp", "the waiter"), true, 5). st_hpd(order("Gavin", "beef and pork fried rice", "the waiter"), true, 5).
```

### Ground Truth
```clingo
waiter("the waiter"). customer("Gavin"). customer("Amandine"). food(f). member("egg drop soup with wonton", f). member("lobster Cantonese", f). member("shrimp, beef and pork fried rice", f). story_step(0..4). st_hpd(lead_to("the waiter", "Gavin", t), true, 0). st_hpd(lead_to("the waiter", "Amandine", t), true, 0). st_hpd(sit("Gavin"), true, 1). st_hpd(sit("Amandine"), true, 1). st_hpd(read_menu("Gavin"), true, 2). st_hpd(read_menu("Amandine"), false). st_hpd(order("Amandine", f, "the waiter"), true, 3). st_hpd(order("Gavin", f, "the waiter"), true, 4).
```

---

## Story #38 — Partial Match (Similarity: 0.0909)

**Story:** One day, Andy felt hungry and went to the RRGrill restaurant for dinner. The restaurant was open and the waiter led Andy to a table. Andy went through the whole menu, but he didn't find any dish that he liked. Andy decided to leave.

### Predicted
```clingo
restaurant("RRGrill restaurant"). customer("Andy"). person("Andy"). waiter("the waiter"). st_obs(hungry("Andy"), true, 0). st_obs(open("RRGrill restaurant"), true, 1). st_hpd(enter("Andy", "RRGrill restaurant"), true, 2). st_obs(in("Andy", "RRGrill restaurant"), true, 2). st_hpd(lead_to("the waiter", "Andy", t), true, 3). st_obs(at_l("Andy", t), true, 3). st_hpd(read_menu("Andy"), true, 4). st_obs(menu_read("Andy"), true, 4). st_hpd(order("Andy"), false). st_hpd(leave("Andy"), true, 5). st_obs(in("Andy", "RRGrill restaurant"), false, 5).
```

### Ground Truth
```clingo
restaurant("RRGrill"). customer("Andy"). food("nothing"). waiter("the waiter"). story_step(0..4). st_hpd(enter("Andy", "RRGrill"), true, 0). st_hpd(lead_to("the waiter", "Andy", t), true, 1). st_hpd(put_down("Andy", m, t), true, 2). st_stop_activity("Andy", 3). next_st(2, 3). st_hpd(leave("Andy"), true, 4).
```

---

## Story #33 — Partial Match (Similarity: 0.1000)

**Story:** One day, Andy felt hungry and went to the RRGrill restaurant for dinner. The restaurant was open, but there was no table available for Andy.

### Predicted
```clingo
restaurant("RRGrill restaurant"). customer("Andy"). person("Andy"). st_obs(hungry("Andy"), true, 0). st_obs(open("RRGrill restaurant"), true, 1). st_obs(at_l(t, "RRGrill restaurant"), false, 1). st_hpd(enter("Andy", "RRGrill restaurant"), true, 2). st_obs(in("Andy", "RRGrill restaurant"), true, 2).
```

### Ground Truth
```clingo
restaurant("RRGrill"). customer("Andy"). story_step(0..1). st_hpd(enter("Andy", "RRGrill"), true, 0). st_obs(table_available, false, 1).
```

---

## Story #39 — Partial Match (Similarity: 0.1000)

**Story:** One day, Andy felt hungry and went to the RRGrill restaurant for dinner. The restaurant was open. The waiter led him to a table. As Andy was sitting down before having a chance to order, he received an emergency phone call and had to leave.

### Predicted
```clingo
restaurant("RRGrill restaurant"). customer("Andy"). person("Andy"). waiter("the waiter"). st_obs(hungry("Andy"), true, 0). st_obs(open("RRGrill restaurant"), true, 1). st_hpd(enter("Andy", "RRGrill restaurant"), true, 2). st_obs(in("Andy", "RRGrill restaurant"), true, 2). st_hpd(lead_to("the waiter", "Andy", t), true, 3). st_obs(at_l("Andy", t), true, 3). st_hpd(sit("Andy"), true, 4). st_obs(sitting("Andy"), true, 4). st_hpd(order("Andy"), false). st_hpd(leave("Andy"), true, 5). st_obs(in("Andy", "RRGrill restaurant"), false, 5).
```

### Ground Truth
```clingo
restaurant("RRGrill"). customer("Andy"). waiter("the waiter"). story_step(0..3). st_hpd(enter("Andy", "RRGrill"), true, 0). st_hpd(lead_to("the waiter", "Andy", t), true, 1). st_obs(sitting("Andy"), true, 2). st_stop_activity("Andy", 2). st_hpd(leave("Andy"), true, 3).
```

---

## Story #90 — Partial Match (Similarity: 0.1176)

**Story:** [REDACTED — original ROCStories text; storyid=c4078b0f-e1c3-4c75-a05a-a52c9481fc2a]

### Predicted
```clingo
restaurant("the restaurant on the Ohio river"). customer("my family"). person("my family"). food("five course meal"). food("bread"). food("salmon"). food("asparagus"). st_obs(in("my family", "the restaurant on the Ohio river"), true, 0). st_obs(available("five course meal", "the restaurant on the Ohio river"), true, 0). st_hpd(eat("people", "bread"), true, 1). st_hpd(eat("I", "salmon"), true, 2). st_hpd(eat("I", "asparagus"), true, 3).
```

### Ground Truth
```clingo
restaurant("a restaurant"). customer("My family"). customer("I"). food("bread"). food("salmon and asparagus"). st_hpd(enter("My family", "a restaurant"), true, 0). st_hpd(eat("My family", "bread"), true, 1). st_hpd(eat("I", "salmon and asparagus"), true, 1).
```

---

## Story #20 — Partial Match (Similarity: 0.1212)

**Story:** The waiter brought out escargot for Molly and me. Then the waiter brought out twelve oysters and twelve clams. We shared the clams and oysters. The waiter poured wine for us.

### Predicted
```clingo
restaurant(r). customer("Molly"). customer("me"). person("Molly"). person("me"). waiter("the waiter"). food("escargot"). food("twelve oysters"). food("twelve clams"). beverage("wine"). member("Molly", "group"). member("me", "group"). member("twelve oysters", "shared_food"). member("twelve clams", "shared_food"). st_hpd(bring("the waiter", "escargot", "Molly"), true, 0). st_hpd(bring("the waiter", "escargot", "me"), true, 0). st_hpd(bring("the waiter", "twelve oysters", "group"), true, 1). st_hpd(bring("the waiter", "twelve clams", "group"), true, 1). st_hpd(eat("Molly", "twelve oysters"), true, 2). st_hpd(eat("me", "twelve oysters"), true, 2). st_hpd(eat("Molly", "twelve clams"), true, 2). st_hpd(eat("me", "twelve clams"), true, 2). st_hpd(pour("the waiter", "wine", "group"), true, 3). st_hpd(drink("Molly", "wine"), true, 4). st_hpd(drink("me", "wine"), true, 4).
```

### Ground Truth
```clingo
restaurant(r). customer(we). member("Molly", we). member(me, we). food(escargot). food(f). member("twelve oysters", f). member("twelve clams", f). beverage("wine"). waiter("the waiter"). story_step(0..3). st_hpd(put_down("the waiter", escargot, t), true, 0). st_hpd(put_down("the waiter", f, t), true, 1). st_hpd(eat(we, f), true, 2). st_hpd(put_down("the waiter", wine, t), true, 3).
```

---

## Story #67 — Partial Match (Similarity: 0.1282)

**Story:** Maria and Leo entered a quiet Italian restaurant. The waiter seated them at a corner table. They ordered a bottle of red wine. After the waiter brought the wine, they ordered two pasta dishes. They enjoyed their meal, paid the bill, and left.

### Predicted
```clingo
person("Maria"). customer("Maria"). person("Leo"). customer("Leo"). waiter("the waiter"). restaurant("a quiet Italian restaurant"). beverage("red wine"). food("two pasta dishes"). st_hpd(enter("Maria", "a quiet Italian restaurant"), true, 0). st_hpd(enter("Leo", "a quiet Italian restaurant"), true, 0). st_hpd(lead_to("the waiter", "Maria", "corner table"), true, 1). st_hpd(lead_to("the waiter", "Leo", "corner table"), true, 1). st_hpd(sit("Maria"), true, 2). st_hpd(sit("Leo"), true, 2). st_hpd(order("Maria", "red wine", "the waiter"), true, 3). st_hpd(order("Leo", "red wine", "the waiter"), true, 3). st_obs(served("Maria"), true, 4). st_obs(served("Leo"), true, 4). st_hpd(order("Maria", "two pasta dishes", "the waiter"), true, 5). st_hpd(order("Leo", "two pasta dishes", "the waiter"), true, 5). st_hpd(eat("Maria", "two pasta dishes"), true, 6). st_hpd(eat("Leo", "two pasta dishes"), true, 6). st_hpd(drink("Maria", "red wine"), true, 6). st_hpd(drink("Leo", "red wine"), true, 6). st_hpd(pay("Maria", b), true, 7). st_hpd(pay("Leo", b), true, 7). st_hpd(leave("Maria"), true, 8). st_hpd(leave("Leo"), true, 8).
```

### Ground Truth
```clingo
restaurant("quiet Italian restaurant"). customer(they). person("Maria"). person("Leo"). member("Maria", they). member("Leo", they). beverage("red wine"). food("pasta dishes"). waiter("the waiter"). story_step(0..7). st_hpd(enter(they, "quiet Italian restaurant"), true, 0). st_hpd(lead_to("the waiter", they, t), true, 1). st_hpd(order(they, "red wine", "the waiter"), true, 2). st_hpd(put_down("the waiter", "red wine", t), true, 3). st_hpd(order(they, "pasta dishes", "the waiter"), true, 4). st_hpd(eat(they, "pasta dishes"), true, 5). st_hpd(drink(they, "red wine"), true, 5). st_hpd(pay(they, b), true, 6). st_hpd(leave(they), true, 7).
```

---

## Story #64 — Partial Match (Similarity: 0.1364)

**Story:** Penny booked a table for two. She and her friend arrived at the restaurant and were seated immediately. They perused the menu, ordered their food, and had a lovely meal.

### Predicted
```clingo
person("Penny"). customer("Penny"). person("her friend"). customer("her friend"). restaurant("the restaurant"). st_hpd(enter("Penny", "the restaurant"), true, 0). st_hpd(enter("her friend", "the restaurant"), true, 0). st_hpd(sit("Penny"), true, 1). st_hpd(sit("her friend"), true, 1). st_hpd(read_menu("Penny"), true, 2). st_hpd(read_menu("her friend"), true, 2). st_hpd(order("Penny", f, w), true, 3). st_hpd(order("her friend", f, w), true, 3). st_hpd(eat("Penny", f), true, 4). st_hpd(eat("her friend", f), true, 4).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer(they). person("Penny"). person("her friend"). member("Penny", they). member("her friend", they). food("food"). story_step(0..5). st_hpd(enter(they, "the restaurant"), true, 0). st_hpd(sit(they), true, 1). st_hpd(read_menu(they), true, 3). st_hpd(order(they, "food", w), true, 4). st_hpd(eat(they, "food"), true, 5).
```

---

## Story #78 — Partial Match (Similarity: 0.1379)

**Story:** [REDACTED — original ROCStories text; storyid=02fbf49d-54f4-493d-b4af-609cc1e23a22]

### Predicted
```clingo
restaurant("diner"). customer("Betsy"). person("Betsy"). waiter("waitress"). food("pancakes"). food("bacon"). beverage("coffee"). st_hpd(enter("Betsy", "diner"), true, 0). st_hpd(order("Betsy", "pancakes", "waitress"), true, 1). st_hpd(order("Betsy", "bacon", "waitress"), true, 2). st_hpd(order("Betsy", "coffee", "waitress"), true, 3). st_hpd(move("waitress", w, t), true, 4). st_obs(holding("waitress", "pancakes"), true, 4). st_obs(holding("waitress", "bacon"), true, 4). st_obs(holding("waitress", "coffee"), true, 4). st_hpd(put_down("waitress", "pancakes", t), true, 5). st_hpd(put_down("waitress", "bacon", t), true, 5). st_hpd(put_down("waitress", "coffee", t), true, 5). st_hpd(eat("Betsy", "pancakes"), true, 6). st_hpd(eat("Betsy", "bacon"), true, 6). st_hpd(drink("Betsy", "coffee"), true, 6). st_hpd(pay("Betsy", tip), true, 7).
```

### Ground Truth
```clingo
restaurant("a diner"). customer("Betsy"). food(f). member("pancakes", f). member("bacon", f). beverage("coffee"). waiter("the waitress"). st_hpd(order("Betsy", f, "the waitress"), true, 0). st_hpd(order("Betsy", "coffee", "the waitress"), true, 0). st_hpd(eat("Betsy", f), true, 1). st_hpd(drink("Betsy", "coffee"), true, 1). st_hpd(pay("Betsy", tip), true, 2).
```

---

## Story #28 — Partial Match (Similarity: 0.1429)

**Story:** One day, Andy felt hungry, and went to the RRGrill restaurant for dinner. The restaurant was open, so he walked into the restaurant where he was greeted by the waiter and was led to the table. Andy ordered soup and he ate it with pleasure. He paid cash and left.

### Predicted
```clingo
restaurant("RRGrill restaurant"). customer("Andy"). person("Andy"). waiter("the waiter"). food("soup"). st_obs(hungry("Andy"), true, 0). st_obs(open("RRGrill restaurant"), true, 1). st_hpd(enter("Andy", "RRGrill restaurant"), true, 2). st_hpd(greet("the waiter", "Andy"), true, 3). st_hpd(lead_to("the waiter", "Andy", t), true, 4). st_hpd(order("Andy", "soup", "the waiter"), true, 5). st_hpd(eat("Andy", "soup"), true, 6). st_hpd(pay("Andy", b), true, 7). st_hpd(leave("Andy"), true, 8).
```

### Ground Truth
```clingo
restaurant("RRGrill"). customer(andy). food(soup). waiter("the waiter"). story_step(0..4). st_hpd(enter(andy, "RRGrill"), true, 0). st_hpd(greet("the waiter", andy), true, 1). st_hpd(lead_to("the waiter", andy, t), true, 2). st_hpd(order(andy, soup, "the waiter"), true, 3). st_hpd(eat(andy, soup), true, 4). st_hpd(pay(andy, b), true, 5). st_hpd(leave(andy), true, 6).
```

---

## Story #51 — Partial Match (Similarity: 0.1429)

**Story:** Steve and his son entered a pizzeria. The waiter took them to a table by the window. They ordered a large pepperoni pizza to share. After eating, Steve paid the bill.

### Predicted
```clingo
person("Steve"). person("his son"). customer("Steve"). customer("his son"). waiter("the waiter"). food("large pepperoni pizza"). restaurant("pizzeria"). member("Steve", "group"). member("his son", "group"). member("large pepperoni pizza", "order_group"). st_hpd(enter("Steve", "pizzeria"), true, 0). st_hpd(enter("his son", "pizzeria"), true, 0). st_hpd(greet("the waiter", "Steve"), true, 1). st_hpd(greet("the waiter", "his son"), true, 1). st_hpd(lead_to("the waiter", "Steve", t), true, 2). st_hpd(lead_to("the waiter", "his son", t), true, 2). st_hpd(sit("Steve"), true, 3). st_hpd(sit("his son"), true, 3). st_hpd(order("Steve", "large pepperoni pizza", "the waiter"), true, 4). st_hpd(eat("Steve", "large pepperoni pizza"), true, 5). st_hpd(eat("his son", "large pepperoni pizza"), true, 5). st_hpd(pay("Steve", b), true, 6). st_obs(in("Steve", "pizzeria"), true, 0). st_obs(in("his son", "pizzeria"), true, 0). st_obs(at_l("Steve", t), true, 2). st_obs(at_l("his son", t), true, 2). st_obs(sitting("Steve"), true, 3). st_obs(sitting("his son"), true, 3). st_obs(paid(b), true, 6).
```

### Ground Truth
```clingo
restaurant("pizzeria"). customer(they). person("Steve"). person("his son"). member("Steve", they). member("his son", they). food("large pepperoni pizza"). waiter("the waiter"). story_step(0..4). st_hpd(enter(they, "pizzeria"), true, 0). st_hpd(lead_to("the waiter", they, t), true, 1). st_hpd(order(they, "large pepperoni pizza", "the waiter"), true, 2). st_hpd(eat(they, "large pepperoni pizza"), true, 3). st_hpd(pay("Steve", b), true, 4).
```

---

## Story #99 — Partial Match (Similarity: 0.1429)

**Story:** [REDACTED — original ROCStories text; storyid=11cd400e-b2b8-4279-9e2e-925de49fee44]

### Predicted
```clingo
restaurant("new Mexican restaurant"). customer("the family"). person("the family"). food("tacos"). food("chicken tacos"). st_hpd(enter("the family", "new Mexican restaurant"), true, 0). st_hpd(order("the family", "tacos", w), true, 1). st_hpd(order("the family", "chicken tacos", w), true, 2). st_hpd(eat("the family", "tacos"), true, 3). st_hpd(eat("the family", "chicken tacos"), true, 4).
```

### Ground Truth
```clingo
restaurant("new restaurant"). customer("The family"). food("different foods"). food("tacos"). st_hpd(enter("The family", "new restaurant"), true, 0). st_hpd(order("The family", "different foods", w), true, 1). st_hpd(eat("The family", "different foods"), true, 2).
```

---

## Story #74 — Partial Match (Similarity: 0.1471)

**Story:** Lisa and Mark went to the Italian restaurant for their date night. They were seated at a cozy table. Lisa ordered lasagna and Mark ordered chicken parmesan. They shared a bottle of wine with their meal.

### Predicted
```clingo
restaurant("Italian restaurant"). customer("Lisa"). customer("Mark"). person("Lisa"). person("Mark"). food("lasagna"). food("chicken parmesan"). beverage("bottle of wine"). member("Lisa", "Lisa and Mark"). member("Mark", "Lisa and Mark"). st_hpd(enter("Lisa and Mark", "Italian restaurant"), true, 0). st_hpd(lead_to(w, "Lisa and Mark", t), true, 1). st_hpd(order("Lisa", "lasagna", w), true, 2). st_hpd(order("Mark", "chicken parmesan", w), true, 3). st_hpd(order("Lisa and Mark", "bottle of wine", w), true, 4). st_hpd(move(w, w, t), true, 5). st_obs(holding(w, "lasagna"), true, 5). st_obs(holding(w, "chicken parmesan"), true, 5). st_obs(holding(w, "bottle of wine"), true, 5). st_hpd(put_down(w, "lasagna", t), true, 6). st_hpd(put_down(w, "chicken parmesan", t), true, 6). st_hpd(put_down(w, "bottle of wine", t), true, 6). st_hpd(eat("Lisa", "lasagna"), true, 7). st_hpd(eat("Mark", "chicken parmesan"), true, 7). st_hpd(drink("Lisa and Mark", "bottle of wine"), true, 7).
```

### Ground Truth
```clingo
restaurant("Italian restaurant"). customer("Lisa"). customer("Mark"). customer(they). member("Lisa", they). member("Mark", they). food("lasagna"). food("chicken parmesan"). beverage("wine"). st_hpd(enter(they, "Italian restaurant"), true, 0). st_obs(sitting(they), true, 1). st_hpd(order("Lisa", "lasagna", "the waiter"), true, 2). st_hpd(order("Mark", "chicken parmesan", "the waiter"), true, 2). st_hpd(eat("Lisa", "lasagna"), true, 3). st_hpd(eat("Mark", "chicken parmesan"), true, 3). st_hpd(drink(they, "wine"), true, 3).
```

---

## Story #13 — Partial Match (Similarity: 0.1515)

**Story:** Judy looked at the menu. She and her two kids, Alex and Zoe, were seated in a booth in a local restaurant. They ordered fish and chips.

### Predicted
```clingo
restaurant("a local restaurant"). customer("Judy"). customer("Alex"). customer("Zoe"). person("Judy"). person("Alex"). person("Zoe"). food("fish and chips"). waiter("the waiter"). st_hpd(enter("Judy", "a local restaurant"), true, 0). st_hpd(enter("Alex", "a local restaurant"), true, 0). st_hpd(enter("Zoe", "a local restaurant"), true, 0). st_obs(in("Judy", "a local restaurant"), true, 0). st_obs(in("Alex", "a local restaurant"), true, 0). st_obs(in("Zoe", "a local restaurant"), true, 0). st_hpd(sit("Judy"), true, 1). st_hpd(sit("Alex"), true, 1). st_hpd(sit("Zoe"), true, 1). st_obs(sitting("Judy"), true, 1). st_obs(sitting("Alex"), true, 1). st_obs(sitting("Zoe"), true, 1). st_obs(at_l("Judy", t), true, 1). st_obs(at_l("Alex", t), true, 1). st_obs(at_l("Zoe", t), true, 1). st_hpd(pick_up("Judy", "the menu", t), true, 2). st_hpd(read_menu("Judy"), true, 3). st_obs(menu_read("Judy"), true, 3). st_hpd(order("Judy", "fish and chips", "the waiter"), true, 4). st_hpd(order("Alex", "fish and chips", "the waiter"), true, 4). st_hpd(order("Zoe", "fish and chips", "the waiter"), true, 4).
```

### Ground Truth
```clingo
restaurant("a local restaurant"). person("Judy"). person("Alex"). person("Zoe"). customer("they"). member("Judy", "they"). member("Alex", "they"). member("Zoe", "they"). food("fish and chips"). story_step(0..1). st_obs(sitting("they"), true, 0). st_hpd(order("they", "fish and chips", w), true, 1).
```

---

## Story #55 — Partial Match (Similarity: 0.1515)

**Story:** Mark and Lisa went to their favorite sushi restaurant. They were seated at the sushi bar. Mark ordered tuna rolls and Lisa ordered salmon nigiri. The chef prepared their order in front of them.

### Predicted
```clingo
person("Mark"). person("Lisa"). customer("Mark"). customer("Lisa"). cook("the chef"). food("tuna rolls"). food("salmon nigiri"). restaurant("sushi restaurant"). st_hpd(enter("Mark", "sushi restaurant"), true, 0). st_hpd(enter("Lisa", "sushi restaurant"), true, 0). st_hpd(lead_to("the host", "Mark", "sushi bar"), true, 1). st_hpd(lead_to("the host", "Lisa", "sushi bar"), true, 1). st_hpd(sit("Mark"), true, 2). st_hpd(sit("Lisa"), true, 2). st_hpd(order("Mark", "tuna rolls", "the waiter"), true, 3). st_hpd(order("Lisa", "salmon nigiri", "the waiter"), true, 4). st_hpd(prepare("the chef", "tuna rolls", "the waiter"), true, 5). st_hpd(prepare("the chef", "salmon nigiri", "the waiter"), true, 5). st_obs(in("Mark", "sushi restaurant"), true, 0). st_obs(in("Lisa", "sushi restaurant"), true, 0). st_obs(at_l("Mark", "sushi bar"), true, 1). st_obs(at_l("Lisa", "sushi bar"), true, 1). st_obs(sitting("Mark"), true, 2). st_obs(sitting("Lisa"), true, 2). st_obs(food_prepared("the chef", "tuna rolls", "the waiter"), true, 5). st_obs(food_prepared("the chef", "salmon nigiri", "the waiter"), true, 5).
```

### Ground Truth
```clingo
restaurant("sushi restaurant"). waiter(w). person("Mark"). person("Lisa"). customer("they"). member("Mark", "they"). member("Mark", "they"). food("tuna rolls"). food("salmon nigiri"). story_step(0..4). st_hpd(enter("they", "sushi restaurant"), true, 0). st_obs(sitting("they"), true, 1). st_hpd(order("Mark", "tuna rolls", w), true, 2). st_hpd(order("Lisa", "salmon nigiri", w), true, 2). st_hpd(prepare("the chef", "tuna rolls", w), true, 3). st_hpd(prepare("the chef", "salmon nigiri", w), true, 3).
```

---

## Story #35 — Partial Match (Similarity: 0.1538)

**Story:** One day, Andy felt hungry and went to the RRGrill restaurant for dinner. The restaurant was open, but there was no table available for Andy. Andy decided to leave.

### Predicted
```clingo
restaurant("RRGrill restaurant"). customer("Andy"). person("Andy"). st_obs(hungry("Andy"), true, 0). st_obs(open("RRGrill restaurant"), true, 1). st_obs(at_l(t, "RRGrill restaurant"), false, 1). st_hpd(enter("Andy", "RRGrill restaurant"), true, 2). st_obs(in("Andy", "RRGrill restaurant"), true, 2). st_hpd(leave("Andy"), true, 3). st_obs(in("Andy", "RRGrill restaurant"), false, 3).
```

### Ground Truth
```clingo
restaurant("RRGrill"). customer("Andy"). story_step(0..3). st_hpd(enter("Andy", "RRGrill"), true, 0). st_hpd(lead_to(w, "Andy", t), false). stop_activity("Andy", 2). st_hpd(leave("Andy"), true, 3).
```

---

## Story #52 — Partial Match (Similarity: 0.1538)

**Story:** David walked into the seafood restaurant and was shown to his table. He browsed the menu and ordered grilled salmon with vegetables. The food arrived quickly. David ate his meal and paid the bill before leaving.

### Predicted
```clingo
person("David"). customer("David"). food("grilled salmon with vegetables"). restaurant("seafood restaurant"). st_hpd(enter("David", "seafood restaurant"), true, 0). st_hpd(lead_to("the host", "David", t), true, 1). st_hpd(sit("David"), true, 2). st_hpd(pick_up("David", "menu", t), true, 3). st_hpd(read_menu("David"), true, 4). st_hpd(put_down("David", "menu", t), true, 5). st_hpd(order("David", "grilled salmon with vegetables", "the waiter"), true, 6). st_hpd(eat("David", "grilled salmon with vegetables"), true, 7). st_hpd(pay("David", b), true, 8). st_hpd(leave("David"), true, 9). st_obs(in("David", "seafood restaurant"), true, 0). st_obs(at_l("David", t), true, 1). st_obs(sitting("David"), true, 2). st_obs(menu_read("David"), true, 4). st_obs(served("David"), true, 7). st_obs(paid(b), true, 8).
```

### Ground Truth
```clingo
restaurant("seafood restaurant"). customer("David"). food("grilled salmon with vegetables"). waiter("the waiter"). st_hpd(enter("David", "seafood restaurant"), true, 0). st_hpd(lead_to("the waiter", "David", t), true, 1). st_hpd(order("David", "grilled salmon with vegetables", "the waiter"), true, 2). st_hpd(put_down("the waiter", "grilled salmon with vegetables", t), true, 3). st_hpd(eat("David", "grilled salmon with vegetables"), true, 4). st_hpd(pay("David", b), true, 5). st_hpd(leave("David"), true, 6).
```

---

## Story #36 — Partial Match (Similarity: 0.1579)

**Story:** One day, Andy felt hungry and went to the RRGrill restaurant for dinner. The restaurant was open and Tom, Andyâ€™s friend, had his birthday party in there. Tom had prepaid for all the food that was offered. The waiter led Andy to Tomâ€™s table. Andy joined the party.

### Predicted
```clingo
restaurant("RRGrill restaurant"). customer("Andy"). person("Andy"). person("Tom"). waiter("the waiter"). st_obs(hungry("Andy"), true, 0). st_obs(open("RRGrill restaurant"), true, 1). st_hpd(enter("Andy", "RRGrill restaurant"), true, 2). st_obs(in("Andy", "RRGrill restaurant"), true, 2). st_obs(in("Tom", "RRGrill restaurant"), true, 3). st_obs(paid(b), true, 4). st_hpd(lead_to("the waiter", "Andy", t), true, 5). st_obs(at_l("Andy", t), true, 5). st_hpd(join("Andy", "Tom"), true, 6).
```

### Ground Truth
```clingo
restaurant("RRGrill"). customer("Andy"). person("Tom"). food("all the food"). waiter("the waiter"). story_step(0..2). st_hpd(enter("Andy", "RRGrill"), true, 0). st_hpd(lead_to("the waiter", "Andy", t), true, 1). st_obs(informed("the waiter", "all the food", "Andy"), true, 2). st_hpd(pay("Tom", b), 2).
```

---

## Story #73 — Partial Match (Similarity: 0.1600)

**Story:** David entered the deli and took a seat at the counter. He ordered a pastrami sandwich and a pickle. The cook prepared his sandwich and the server brought it to him. David ate his lunch quickly.

### Predicted
```clingo
restaurant("deli"). customer("David"). person("David"). cook("cook"). waiter("server"). food("pastrami sandwich"). food("pickle"). st_hpd(enter("David", "deli"), true, 0). st_hpd(sit("David"), true, 1). st_hpd(order("David", "pastrami sandwich", "server"), true, 2). st_hpd(order("David", "pickle", "server"), true, 3). st_hpd(prepare("cook", "pastrami sandwich", "server"), true, 4). st_hpd(move("server", w, t), true, 5). st_obs(holding("server", "pastrami sandwich"), true, 5). st_obs(holding("server", "pickle"), true, 5). st_hpd(put_down("server", "pastrami sandwich", t), true, 6). st_hpd(put_down("server", "pickle", t), true, 6). st_hpd(eat("David", "pastrami sandwich"), true, 7). st_hpd(eat("David", "pickle"), true, 7).
```

### Ground Truth
```clingo
restaurant("the deli"). customer("David"). food(f). member("pastrami sandwich", f). member("pickle", f). st_hpd(enter("David", "the deli"), true, 0). st_hpd(sit("David"), true, 1). st_hpd(order("David", f, "the server"), true, 2). st_hpd(prepare("the cook", f, "the server"), true, 3). st_hpd(put_down("the server", f, t), true, 4). st_hpd(eat("David", f), true, 5).
```

---

## Story #75 — Partial Match (Similarity: 0.1600)

**Story:** [REDACTED — original ROCStories text; storyid=99d073a9-375a-45ad-a070-0fdfbbf73f69]

### Predicted
```clingo
restaurant("Sushi place"). customer("I"). customer("my husband"). person("I"). person("my husband"). food("spicy tuna rolls"). food("eel"). member("I", "we"). member("my husband", "we"). st_hpd(enter("we", "Sushi place"), true, 0). st_hpd(order("we", "spicy tuna rolls", w), true, 1). st_hpd(order("we", "eel", w), true, 2). st_hpd(move(w, w, t), true, 3). st_obs(holding(w, "spicy tuna rolls"), true, 3). st_obs(holding(w, "eel"), true, 3). st_hpd(put_down(w, "spicy tuna rolls", t), true, 4). st_hpd(put_down(w, "eel", t), true, 4). st_hpd(eat("we", "spicy tuna rolls"), true, 5). st_hpd(eat("we", "eel"), true, 5).
```

### Ground Truth
```clingo
restaurant("new Sushi place"). customer(we). person("I"). person("my husband"). member("I", we). member("my husband", we). food(f). member("spicy tuna rolls", f). member("eel", f). st_hpd(enter(we, "new Sushi place"), true, 0). st_hpd(order(we, f, w), true, 1). st_hpd(eat(we, f), true, 2).
```

---

## Story #2 — Partial Match (Similarity: 0.1667)

**Story:** John enters the restaurant. The waiter escorts him to a table. John orders steak. The waiter brings the steak to the table. John asks for the bill, and the waiter brings it to the table. John pays the bill and leaves the restaurant.

### Predicted
```clingo
restaurant("the restaurant"). customer("John"). person("John"). waiter("the waiter"). food("steak"). st_hpd(enter("John", "the restaurant"), true, 0). st_hpd(greet("the waiter", "John"), true, 1). st_hpd(lead_to("the waiter", "John", t), true, 2). st_hpd(sit("John"), true, 3). st_hpd(order("John", "steak", "the waiter"), true, 4). st_hpd(prepare(c, "steak", "the waiter"), true, 5). st_obs(food_prepared(c, "steak", "the waiter"), true, 5). st_hpd(move("the waiter", l1, t), true, 6). st_hpd(put_down("the waiter", "steak", t), true, 6). st_obs(served("John"), true, 6). st_hpd(eat("John", "steak"), true, 7). st_hpd(request("John", b, "the waiter"), true, 8). st_hpd(move("the waiter", l2, t), true, 9). st_hpd(put_down("the waiter", b, t), true, 9). st_obs(bill_generated("John", b), true, 9). st_hpd(pay("John", b), true, 10). st_obs(paid(b), true, 10). st_hpd(stand_up("John"), true, 11). st_hpd(leave("John"), true, 12).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer("John"). food("steak"). waiter("the waiter"). story_step(0..6). st_hpd(enter("John", "the restaurant"), true, 0). st_hpd(lead_to("the waiter", "John", t), true, 1). st_hpd(order("John", "steak", "the waiter"), true, 2). st_hpd(put_down("the waiter", "steak", t), true, 3). st_hpd(request("John", b, "the waiter"), true, 4). st_hpd(put_down("the waiter", b, t), true, 5). st_hpd(pay("John", b), true, 6). st_hpd(leave("John"), true, 7).
```

---

## Story #5 — Partial Match (Similarity: 0.1667)

**Story:** The waiter shows Jane to her table. Jane is seated at a table in the restaurant. The waiter asks for her order, and she orders fish. After eating, the waiter brings the bill to the table.

### Predicted
```clingo
restaurant("the restaurant"). customer("Jane"). person("Jane"). waiter("the waiter"). food("fish"). st_hpd(greet("the waiter", "Jane"), true, 0). st_hpd(lead_to("the waiter", "Jane", t), true, 1). st_hpd(sit("Jane"), true, 2). st_obs(sitting("Jane"), true, 2). st_hpd(greet("the waiter", "Jane"), true, 3). st_hpd(order("Jane", "fish", "the waiter"), true, 4). st_hpd(prepare(c, "fish", "the waiter"), true, 5). st_obs(food_prepared(c, "fish", "the waiter"), true, 5). st_hpd(move("the waiter", l1, t), true, 6). st_hpd(put_down("the waiter", "fish", t), true, 6). st_obs(served("Jane"), true, 6). st_hpd(eat("Jane", "fish"), true, 7). st_hpd(move("the waiter", l2, t), true, 8). st_hpd(put_down("the waiter", b, t), true, 8). st_obs(bill_generated("Jane", b), true, 8).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer("Jane"). food("fish"). waiter("the waiter"). story_step(0..4). st_hpd(lead_to("the waiter", "Jane", t), true, 0). st_obs(sitting("Jane"), true, 1). st_hpd(order("Jane", "fish", "the waiter"), true, 2). st_hpd(eat("Jane", "fish"), true, 3). st_hpd(put_down("the waiter", b, t), true, 4).
```

---

## Story #37 — Partial Match (Similarity: 0.1667)

**Story:** One day, Andy felt hungry and went to the RRGrill restaurant for dinner. The restaurant was closed that day. He decided to go to Happy Pizza instead.

### Predicted
```clingo
restaurant("RRGrill restaurant"). restaurant("Happy Pizza"). customer("Andy"). person("Andy"). st_obs(hungry("Andy"), true, 0). st_obs(open("RRGrill restaurant"), false, 1). st_hpd(enter("Andy", "RRGrill restaurant"), false). st_hpd(enter("Andy", "Happy Pizza"), true, 2). st_obs(in("Andy", "Happy Pizza"), true, 2).
```

### Ground Truth
```clingo
restaurant("RRGrill"). restaurant("Happy Pizza"). customer("Andy"). story_step(0..2). st_obs(closed("RRGrill"), true, 0). stop_activity("Andy", 1). st_hpd(move("Andy", "RRGrill", "Happy Pizza"), true, 2).
```

---

## Story #93 — Partial Match (Similarity: 0.1667)

**Story:** [REDACTED — original ROCStories text; storyid=0b8e4ddd-6ada-42ba-9d6f-508db0bac85a]

### Predicted
```clingo
restaurant("the restaurant"). restaurant("Burger King"). customer("me"). customer("my mother"). person("me"). person("my mother"). food("steak"). st_obs(hungry("me"), true, 0). st_obs(hungry("my mother"), true, 0). st_hpd(enter("me", "the restaurant"), true, 1). st_hpd(enter("my mother", "the restaurant"), true, 1). st_hpd(sit("me"), true, 2). st_hpd(sit("my mother"), true, 2). st_hpd(order("me", "steak", w), true, 3). st_obs(available("steak", "the restaurant"), false, 4). st_hpd(leave("me"), true, 5). st_hpd(leave("my mother"), true, 5). st_hpd(enter("me", "Burger King"), true, 6). st_hpd(enter("my mother", "Burger King"), true, 6).
```

### Ground Truth
```clingo
restaurant("the restaurant"). restaurant("Burger King"). customer(we). person("I"). person("my mother"). food("steak"). st_hpd(sit(we), true, 0). st_hpd(order("I", "steak", w), true, 1). st_obs(available("steak", "the restaurant"), false, 1). st_hpd(leave(we), true, 2). st_hpd(enter(we, "Burger King"), true, 3).
```

---

## Story #21 — Partial Match (Similarity: 0.1739)

**Story:** The waiter brought the wine to their table. Then, Emanuel studied the menu. He ordered the gypsy shashlik for Ingrid and himself. After the waiter left, they drank the wine. The waiter brought the shashlik to their table.

### Predicted
```clingo
restaurant(r). customer("Emanuel"). customer("Ingrid"). person("Emanuel"). person("Ingrid"). waiter("the waiter"). food("gypsy shashlik"). beverage("wine"). st_hpd(bring("the waiter", "wine", "table"), true, 0). st_hpd(read_menu("Emanuel"), true, 1). st_hpd(order("Emanuel", "gypsy shashlik", "the waiter"), true, 2). st_hpd(order_for("Emanuel", "Ingrid", "gypsy shashlik", "the waiter"), true, 2). st_hpd(leave("the waiter"), true, 3). st_hpd(drink("Emanuel", "wine"), true, 4). st_hpd(drink("Ingrid", "wine"), true, 4). st_hpd(bring("the waiter", "gypsy shashlik", "table"), true, 5).
```

### Ground Truth
```clingo
restaurant(r). customer(they). member("Emanuel"). member("Ingrid"). beverage(wine). food("gypsy shashlik"). waiter("the waiter"). story_step(0..5). st_hpd(put_down("the waiter", wine, t), true, 0). st_hpd(pick_up("Emanuel", m, t), true, 1). st_hpd(order_for("Emanuel", they, "gypsy shashlik", "the waiter"), true, 2). st_hpd(move("the waiter", t, kitchen), true, 3). st_hpd(drink(they, wine), true, 4). st_hpd(put_down("the waiter", "gypsy shashlik", t), true, 5).
```

---

## Story #94 — Partial Match (Similarity: 0.1818)

**Story:** [REDACTED — original ROCStories text; storyid=63dfd3a4-930a-4a27-8ed9-60304b6c32f3]

### Predicted
```clingo
restaurant("new sushi place"). customer("the couple"). person("the couple"). food("food"). st_obs(hungry("the couple"), true, 0). st_hpd(enter("the couple", "new sushi place"), true, 1). st_hpd(order("the couple", "food", w), true, 2). st_hpd(eat("the couple", "food"), true, 3). st_obs(hungry("the couple"), false, 4).
```

### Ground Truth
```clingo
restaurant("new sushi place"). customer("The couple"). food(f). st_hpd(enter("The couple", "new sushi place"), true, 0). st_hpd(eat("The couple", f), true, 1).
```

---

## Story #14 — Partial Match (Similarity: 0.1875)

**Story:** Samantha was in a five-star restaurant. Samantha started perusing the menu. She ordered the barbecued veal chop with Asian slaw and Thai fried rice.

### Predicted
```clingo
restaurant("a five-star restaurant"). customer("Samantha"). person("Samantha"). food("barbecued veal chop"). food("Asian slaw"). food("Thai fried rice"). waiter("the waiter"). st_obs(in("Samantha", "a five-star restaurant"), true, 0). st_hpd(pick_up("Samantha", "the menu", t), true, 1). st_hpd(read_menu("Samantha"), true, 2). st_obs(menu_read("Samantha"), true, 2). st_hpd(order("Samantha", "barbecued veal chop", "the waiter"), true, 3). st_hpd(order("Samantha", "Asian slaw", "the waiter"), true, 3). st_hpd(order("Samantha", "Thai fried rice", "the waiter"), true, 3).
```

### Ground Truth
```clingo
restaurant("a five-star restaurant"). customer("Samantha"). food("barbecued veal chop with Asian slaw and Thai fried rice"). story_step(0..2). st_obs(in("Samantha", "a five-star restaurant"), true, 0). st_hpd(read_menu("Samantha"), true, 1). st_hpd(order("Samantha", "barbecued veal chop with Asian slaw and Thai fried rice", w), true, 2).
```

---

## Story #18 — Partial Match (Similarity: 0.1875)

**Story:** Herbie and his father were at a meat restaurant. The waiter brought a sizzling steak that smelled heavenly, and a plate with haddock and creamed spinach. The waiter put Herbie's plate down. Herbieâ€™s father asked the waiter to take the fish away and bring the boy some lamb chops instead.

### Predicted
```clingo
restaurant("a meat restaurant"). customer("Herbie"). customer("Herbie's father"). person("Herbie"). person("Herbie's father"). food("sizzling steak"). food("haddock"). food("creamed spinach"). food("lamb chops"). waiter("the waiter"). st_obs(in("Herbie", "a meat restaurant"), true, 0). st_obs(in("Herbie's father", "a meat restaurant"), true, 0). st_hpd(move("the waiter", "the kitchen", t), true, 1). st_obs(holding("the waiter", "sizzling steak"), true, 1). st_obs(holding("the waiter", "haddock"), true, 1). st_obs(holding("the waiter", "creamed spinach"), true, 1). st_hpd(put_down("the waiter", "sizzling steak", t), true, 2). st_hpd(put_down("the waiter", "haddock", t), true, 2). st_hpd(put_down("the waiter", "creamed spinach", t), true, 2). st_hpd(put_down("the waiter", "haddock", t), true, 3). st_obs(served("Herbie"), true, 3). st_hpd(request("Herbie's father", "lamb chops", "the waiter"), true, 4). st_hpd(prepare("the cook", "lamb chops", "the waiter"), true, 5). st_hpd(move("the waiter", "the kitchen", t), true, 6). st_obs(holding("the waiter", "lamb chops"), true, 6). st_hpd(put_down("the waiter", "lamb chops", t), true, 7). st_obs(served("Herbie"), true, 7).
```

### Ground Truth
```clingo
restaurant("a meat restaurant"). customer("Herbie"). customer("his father"). food("a sizzling steak"). food("haddock and creamed spinach"). food("lamb chops"). waiter("the waiter"). story_step(0..4). st_obs(in("Herbie", "a meat restaurant"), true, 0). st_obs(in("his father", "a meat restaurant"), true, 0). st_hpd(put_down("the waiter", "a sizzling steak", t), true, 1). st_hpd(put_down("the waiter", "haddock and creamed spinach", t), true, 2). st_hpd(request("his father", pick_up("the waiter", "haddock and creamed spinach", t), "the waiter"), true, 3). st_hpd(order_for("his father", "Herbie", "lamb chops", "the waiter"), true, 4).
```

---

## Story #84 — Partial Match (Similarity: 0.1875)

**Story:** [REDACTED — original ROCStories text; storyid=0f9b69ff-6fbe-4e94-a37a-8ef3fbf2a876]

### Predicted
```clingo
restaurant("the diner"). customer("Donna"). person("Donna"). food("cheeseburger"). food("onion rings"). st_hpd(enter("Donna", "the diner"), true, 0). st_obs(in("Donna", "the diner"), true, 0). st_hpd(order("Donna", "cheeseburger", w), true, 1). st_hpd(order("Donna", "onion rings", w), true, 2). st_hpd(eat("Donna", "cheeseburger"), true, 3). st_hpd(eat("Donna", "onion rings"), true, 4). st_hpd(leave("Donna"), true, 5).
```

### Ground Truth
```clingo
restaurant("diner"). customer("Donna"). food(f). member("cheeseburger", f). member("onion rings", f). st_hpd(enter("Donna", "diner"), true, 0). st_hpd(order("Donna", f, w), true, 1). st_hpd(eat("Donna", f), true, 2).
```

---

## Story #17 — Partial Match (Similarity: 0.2000)

**Story:** The waiter brought his dinner. He was eating something spotted with eggs and livers. He finished but the waiter wouldn't come total the bill.

### Predicted
```clingo
restaurant("the restaurant"). customer("He"). person("He"). food("something spotted with eggs and livers"). waiter("the waiter"). st_hpd(move("the waiter", "the kitchen", t), true, 0). st_obs(holding("the waiter", "something spotted with eggs and livers"), true, 0). st_hpd(put_down("the waiter", "something spotted with eggs and livers", t), true, 1). st_obs(served("He"), true, 1). st_hpd(eat("He", "something spotted with eggs and livers"), true, 2). st_hpd(request("He", b, "the waiter"), true, 3). st_hpd(read_bill("He"), false). st_hpd(pay("He", b), false).
```

### Ground Truth
```clingo
customer("he"). food("something spotted with eggs and livers"). waiter("the waiter"). story_step(0..1). st_hpd(put_down("the waiter", "something spotted with eggs and livers", t), true, 0). st_hpd(eat("he", "something spotted with eggs and livers"), true, 1). st_hpd(put_down("the waiter", b, t), false).
```

---

## Story #79 — Partial Match (Similarity: 0.2000)

**Story:** [REDACTED — original ROCStories text; storyid=845b62e4-9240-4afe-8d59-ae2bc183967c]

### Predicted
```clingo
restaurant("new steakhouse"). customer("The couple"). person("The couple"). food("huge cuts of meat"). member("The couple", "The couple"). st_hpd(enter("The couple", "new steakhouse"), true, 0). st_hpd(order("The couple", "huge cuts of meat", w), true, 1). st_hpd(move(w, w, t), true, 2). st_obs(holding(w, "huge cuts of meat"), true, 2). st_hpd(put_down(w, "huge cuts of meat", t), true, 3). st_hpd(eat("The couple", "huge cuts of meat"), true, 4). st_hpd(read_bill("The couple"), true, 5).
```

### Ground Truth
```clingo
restaurant("new steakhouse"). customer("the couple"). food("huge cuts of meat"). st_obs(in("the couple", "new steakhouse"), true, 0). st_hpd(put_down(w, "huge cuts of meat", t), true, 1). st_hpd(eat("the couple", "huge cuts of meat"), true, 2). st_hpd(put_down(w, b, t), true, 3).
```

---

## Story #83 — Partial Match (Similarity: 0.2000)

**Story:** [REDACTED — original ROCStories text; storyid=9c2ccb82-003d-4253-9f19-65b157b9993f]

### Predicted
```clingo
restaurant("the diner"). customer("the couple"). person("the couple"). waiter("the waitress"). st_hpd(enter("the couple", "the diner"), true, 0). st_obs(in("the couple", "the diner"), true, 0). st_hpd(sit("the couple"), true, 1). st_obs(sitting("the couple"), true, 1). st_hpd(greet(w, "the couple"), false). st_hpd(stand_up("the couple"), true, 2). st_hpd(leave("the couple"), true, 3). st_hpd(greet("the waitress", "the couple"), true, 4). st_hpd(order("the couple", f, "the waitress"), true, 5).
```

### Ground Truth
```clingo
restaurant("diner"). customer("the couple"). waiter("the waitress"). st_hpd(sit("the couple"), true, 0). st_hpd(greet("the waitress", "the couple"), false). st_hpd(stand_up("the couple"), true, 1).
```

---

## Story #91 — Partial Match (Similarity: 0.2000)

**Story:** [REDACTED — original ROCStories text; storyid=ac7250f9-d416-41bb-aac7-b1dd788b86fb]

### Predicted
```clingo
restaurant("fast food restaurant"). customer("Emily"). person("Emily"). person("cashier"). food("fries"). food("burger"). st_obs(in("Emily", "fast food restaurant"), true, 0). st_hpd(order("Emily", "fries", "cashier"), true, 1). st_hpd(order("Emily", "burger", "cashier"), true, 2). st_hpd(prepare("cook", "f", "cashier"), true, 3). st_obs(food_prepared("cook", "f", "cashier"), true, 4). st_obs(available("burger", "fast food restaurant"), true, 5). st_obs(available("fries", "fast food restaurant"), false, 5). st_hpd(complain("Emily", "cashier"), true, 6).
```

### Ground Truth
```clingo
restaurant("fast food restaurant"). customer("Emily"). food("fries"). food("burger"). waiter("the cashier"). st_hpd(order("Emily", "fries", "the cashier"), true, 0). st_hpd(order("Emily", "burger", "the cashier"), true, 0). st_hpd(put_down("the cashier", "burger", t), true, 1). st_hpd(put_down("the cashier", "fries", t), false). st_hpd(complain("Emily", "the cashier"), true, 2). st_next(1,2).
```

---

## Story #53 — Partial Match (Similarity: 0.2093)

**Story:** The Johnson family entered the family restaurant. They were seated in a booth and given menus. Mr. Johnson ordered steak, Mrs. Johnson ordered salad, and their son ordered pizza. The waiter brought all their orders together.

### Predicted
```clingo
person("Mr. Johnson"). person("Mrs. Johnson"). person("their son"). customer("Mr. Johnson"). customer("Mrs. Johnson"). customer("their son"). waiter("the waiter"). food("steak"). food("salad"). food("pizza"). restaurant("family restaurant"). member("Mr. Johnson", "Johnson family"). member("Mrs. Johnson", "Johnson family"). member("their son", "Johnson family"). st_hpd(enter("Mr. Johnson", "family restaurant"), true, 0). st_hpd(enter("Mrs. Johnson", "family restaurant"), true, 0). st_hpd(enter("their son", "family restaurant"), true, 0). st_hpd(lead_to("the waiter", "Mr. Johnson", "booth"), true, 1). st_hpd(lead_to("the waiter", "Mrs. Johnson", "booth"), true, 1). st_hpd(lead_to("the waiter", "their son", "booth"), true, 1). st_hpd(sit("Mr. Johnson"), true, 2). st_hpd(sit("Mrs. Johnson"), true, 2). st_hpd(sit("their son"), true, 2). st_hpd(order("Mr. Johnson", "steak", "the waiter"), true, 3). st_hpd(order("Mrs. Johnson", "salad", "the waiter"), true, 4). st_hpd(order("their son", "pizza", "the waiter"), true, 5). st_obs(in("Mr. Johnson", "family restaurant"), true, 0). st_obs(in("Mrs. Johnson", "family restaurant"), true, 0). st_obs(in("their son", "family restaurant"), true, 0). st_obs(at_l("Mr. Johnson", "booth"), true, 1). st_obs(at_l("Mrs. Johnson", "booth"), true, 1). st_obs(at_l("their son", "booth"), true, 1). st_obs(sitting("Mr. Johnson"), true, 2). st_obs(sitting("Mrs. Johnson"), true, 2). st_obs(sitting("their son"), true, 2).
```

### Ground Truth
```clingo
restaurant("family restaurant"). person("Mr. Johnson"). person("Mrs. Johnson"). person("son"). customer("Johnson family"). member("Mr. Johnson", "Johnson family"). member("Mrs. Johnson", "Johnson family"). member("son", "Johnson family"). food("steak"). food("salad"). food("pizza"). waiter("the waiter"). story_step(0..4). st_hpd(enter("Johnson family", "family restaurant"), true, 0). st_obs(sitting("Johnson family"), true, 1). st_hpd(order("Mr. Johnson", "steak", "the waiter"), true, 2). st_hpd(order("Mrs. Johnson", "salad", "the waiter"), true, 2). st_hpd(order("son", "pizza", "the waiter"), true, 2). st_hpd(put_down("the waiter", "steak", t), true, 3). st_hpd(put_down("the waiter", "salad", t), true, 3). st_hpd(put_down("the waiter", "pizza", t), true, 3).
```

---

## Story #27 — Partial Match (Similarity: 0.2105)

**Story:** Nicole and Sam went to a vegetarian restaurant. She ordered a lentil soup. He ordered a miso soup. They both enjoyed their soups.

### Predicted
```clingo
restaurant("vegetarian restaurant"). customer("Nicole"). customer("Sam"). person("Nicole"). person("Sam"). food("lentil soup"). food("miso soup"). st_hpd(enter("Nicole", "vegetarian restaurant"), true, 0). st_hpd(enter("Sam", "vegetarian restaurant"), true, 0). st_hpd(order("Nicole", "lentil soup", w), true, 1). st_hpd(order("Sam", "miso soup", w), true, 1). st_hpd(eat("Nicole", "lentil soup"), true, 2). st_hpd(eat("Sam", "miso soup"), true, 2).
```

### Ground Truth
```clingo
restaurant(veg_r). customer(nicole). customer(sam). food(lentil_soup). food(miso_soup). waiter(w). story_step(0..3). st_hpd(enter(nicole, veg_r), true, 0). st_hpd(enter(sam, veg_r), true, 0). st_hpd(order(nicole, lentil_soup, waitress), true, 1). st_hpd(order(sam, miso_soup, waitress), true, 2). st_hpd(eat(nicole, lentil_soup), true, 3). st_hpd(eat(sam, miso_soup), true, 3).
```

---

## Story #69 — Partial Match (Similarity: 0.2105)

**Story:** A group of coworkers went to a sandwich shop for lunch. The waiter seated them at a long table, and took their orders. The waiter brought out all the sandwiches. They ate, paid their separate bills, and returned to work.

### Predicted
```clingo
person("A group of coworkers"). customer("A group of coworkers"). waiter("the waiter"). restaurant("a sandwich shop"). food("all the sandwiches"). st_hpd(enter("A group of coworkers", "a sandwich shop"), true, 0). st_hpd(lead_to("the waiter", "A group of coworkers", "long table"), true, 1). st_hpd(sit("A group of coworkers"), true, 2). st_hpd(order("A group of coworkers", "all the sandwiches", "the waiter"), true, 3). st_obs(served("A group of coworkers"), true, 4). st_hpd(eat("A group of coworkers", "all the sandwiches"), true, 5). st_hpd(pay("A group of coworkers", b), true, 6). st_hpd(leave("A group of coworkers"), true, 7).
```

### Ground Truth
```clingo
restaurant("sandwich shop"). customer("group of coworkers"). food("sandwiches"). waiter("the waiter"). st_hpd(enter("group of coworkers", "sandwich shop"), true, 0). st_hpd(lead_to("the waiter", "group of coworkers", t), true, 1). st_hpd(order("group of coworkers", "sandwiches", "the waiter"), true, 2). st_hpd(put_down("the waiter", "sandwiches", t), true, 3). st_hpd(eat("group of coworkers", "sandwiches"), true, 4). st_hpd(pay("group of coworkers", b), true, 5). st_hpd(leave("group of coworkers"), true, 6).
```

---

## Story #97 — Partial Match (Similarity: 0.2105)

**Story:** [REDACTED — original ROCStories text; storyid=d25ec012-9f9f-48e6-8274-e6ac4a4b59e4]

### Predicted
```clingo
restaurant(r). customer("Tim"). person("Tim"). person("waiter"). waiter("waiter"). food("food"). st_obs(in("Tim", r), true, 0). st_hpd(order("Tim", "food", "waiter"), true, 1). st_hpd(prepare("cook", f, "waiter"), true, 2). st_obs(food_prepared("cook", f, "waiter"), true, 3). st_obs(available("food", r), true, 4). st_hpd(complain("Tim", "waiter"), true, 5). st_next(4, 5). st_hpd(prepare("cook", "food", "waiter"), true, 6). st_obs(food_prepared("cook", "food", "waiter"), true, 7).
```

### Ground Truth
```clingo
restaurant(r). customer("Tim"). food("wrong order"). waiter("the waiter"). st_obs(in("Tim", r), true, 0). st_hpd(put_down("the waiter", "wrong order", t), true, 1). st_hpd(complain("Tim", "the waiter"), true, 2). st_next(1, 2). st_hpd(put_down("the waiter", f, t), true, 3).
```

---

## Story #92 — Partial Match (Similarity: 0.2143)

**Story:** [REDACTED — original ROCStories text; storyid=c9e533e3-d8cc-4e9c-a7a0-0369d6cdc537]

### Predicted
```clingo
restaurant("new restaurant in the mall"). customer("I"). person("I"). food("large salad"). st_obs(in("I", "new restaurant in the mall"), true, 0). st_obs(open("new restaurant in the mall"), true, 0). st_hpd(order("I", "large salad", w), true, 1). st_obs(available("large salad", "new restaurant in the mall"), true, 2). st_hpd(eat("I", "large salad"), true, 3). st_obs(open("new restaurant in the mall"), false, 4).
```

### Ground Truth
```clingo
restaurant("new restaurant"). customer("I"). food("large salad"). food("small salad"). waiter(w). st_obs(in("I", "new restaurant"), true, 0). st_hpd(order("I", "large salad", w), true, 1). st_hpd(put_down(w, "small salad", t), true, 2).
```

---

## Story #15 — Partial Match (Similarity: 0.2174)

**Story:** The villager entered a fine restaurant and was seated at one of the tables. He looked at the menu. He ordered one of the items on the list. The waiter brought him a large plate of lettuce salad with several black olives on top.

### Predicted
```clingo
restaurant("a fine restaurant"). customer("The villager"). person("The villager"). food("one of the items on the list"). food("large plate of lettuce salad with several black olives on top"). waiter("the waiter"). st_hpd(enter("The villager", "a fine restaurant"), true, 0). st_obs(in("The villager", "a fine restaurant"), true, 0). st_hpd(sit("The villager"), true, 1). st_obs(sitting("The villager"), true, 1). st_obs(at_l("The villager", t), true, 1). st_hpd(pick_up("The villager", "the menu", t), true, 2). st_hpd(read_menu("The villager"), true, 3). st_obs(menu_read("The villager"), true, 3). st_hpd(order("The villager", "one of the items on the list", "the waiter"), true, 4). st_hpd(prepare("the cook", "large plate of lettuce salad with several black olives on top", "the waiter"), true, 5). st_hpd(move("the waiter", "the kitchen", t), true, 6). st_obs(holding("the waiter", "large plate of lettuce salad with several black olives on top"), true, 6). st_hpd(put_down("the waiter", "large plate of lettuce salad with several black olives on top", t), true, 7). st_obs(served("The villager"), true, 7).
```

### Ground Truth
```clingo
restaurant("a fine restaurant"). customer("the villager"). food("one of the items on the list"). food("lettuce salad with several black olives on top"). story_step(0..4). st_hpd(enter("the villager", "a fine restaurant"), true, 0). st_obs(sitting("the villager"), true, 1). st_hpd(pick_up("the villager", m, t), true, 2). st_hpd(order("the villager", "one of the items on the list", w), true, 3). st_hpd(put_down(w, "lettuce salad with several black olives on top", t), true, 4).
```

---

## Story #22 — Partial Match (Similarity: 0.2174)

**Story:** Andrew was sitting in a restaurant. Sebastian entered the restaurant and sat down opposite Andrew. The waiter brought a bottle of wine. Andrew and Sebastian took a drink. The waiter gave the men a menu.

### Predicted
```clingo
restaurant(r). customer("Andrew"). customer("Sebastian"). person("Andrew"). person("Sebastian"). waiter("the waiter"). beverage("a bottle of wine"). st_obs(sitting("Andrew"), true, 0). st_hpd(enter("Sebastian", r), true, 1). st_hpd(sit("Sebastian"), true, 2). st_hpd(bring("the waiter", "a bottle of wine", "table"), true, 3). st_hpd(drink("Andrew", "a bottle of wine"), true, 4). st_hpd(drink("Sebastian", "a bottle of wine"), true, 4). st_hpd(give("the waiter", "menu", "Andrew"), true, 5). st_hpd(give("the waiter", "menu", "Sebastian"), true, 5).
```

### Ground Truth
```clingo
restaurant("a restaurant"). customer("the men"). person("Andrew"). person("Sebastian"). member("Andrew", "the men"). member("Sebastian", "the men"). beverage(wine). waiter("the waiter"). story_step(0..5). st_obs(in("Andrew", "a restaurant"), true, 0). st_obs(sitting("Andrew"), true, 0). st_hpd(enter("Sebastian", "a restaurant"), true, 1). st_hpd(sit("Sebastian"), true, 2). st_hpd(put_down("the waiter", wine, t), true, 3). st_hpd(drink("the men", wine), true, 4). st_hpd(put_down("the waiter", m, t), true, 5).
```

---

## Story #32 — Partial Match (Similarity: 0.2222)

**Story:** Nicole went to a vegetarian restaurant. She ordered a lentil soup. Nicole was in a hurry, so as soon as the waitress laid the dish on the table, Nicole paid for it in cash and said that she didn't need the bill.

### Predicted
```clingo
restaurant("vegetarian restaurant"). customer("Nicole"). person("Nicole"). food("lentil soup"). waiter("the waitress"). st_obs(in("Nicole", "vegetarian restaurant"), true, 0). st_hpd(order("Nicole", "lentil soup", "the waitress"), true, 1). st_hpd(prepare(cook, "lentil soup", "the waitress"), true, 2). st_obs(food_prepared(cook, "lentil soup", "the waitress"), true, 2). st_obs(at_l("lentil soup", t), true, 3). st_hpd(pay("Nicole", b), true, 4). st_obs(paid(b), true, 4). st_hpd(request("Nicole", "the bill", "the waitress"), false).
```

### Ground Truth
```clingo
restaurant(veg_r). customer(nicole). person(owner). food(lentil_soup). waiter(waitress). story_step(0..3). st_hpd(enter(nicole, veg_r), true, 0). st_hpd(order(nicole, lentil_soup, waitress), true, 1). st_hpd(put_down(waitress, miso_soup, t), true, 2). st_hpd(pay(nicole, b), true, 3). next_st(2, 3).
```

---

## Story #47 — Partial Match (Similarity: 0.2222)

**Story:** Gary went to a restaurant for his birthday. He ordered a steak. After he finished eating, the waiter surprised him with a small cake, on the house. Gary left a large tip.

### Predicted
```clingo
restaurant(r). customer("Gary"). person("Gary"). food("steak"). food("cake"). waiter("the waiter"). st_obs(in("Gary", r), true, 0). st_hpd(order("Gary", "steak", "the waiter"), true, 1). st_hpd(prepare("cook", "steak", "the waiter"), true, 2). st_hpd(eat("Gary", "steak"), true, 3). st_hpd(prepare("cook", "cake", "the waiter"), true, 4). st_hpd(eat("Gary", "cake"), true, 5). st_hpd(pay("Gary", tip), true, 6). st_hpd(leave("Gary"), true, 7).
```

### Ground Truth
```clingo
restaurant("a restaurant"). customer("Gary"). food("steak"). food("cake"). waiter("the waiter"). story_step(0..3). st_hpd(order("Gary", "steak", "the waiter"), true, 0). st_hpd(eat("Gary", "steak"), true, 1). st_hpd(put_down("the waiter", "cake", t), true, 2). st_hpd(pay("Gary", tip), true, 3).
```

---

## Story #77 — Partial Match (Similarity: 0.2222)

**Story:** [REDACTED — original ROCStories text; storyid=44b80dab-a351-4065-86b8-43d519dff470]

### Predicted
```clingo
restaurant("new restaurant"). customer("Karl"). customer("his wife"). person("Karl"). person("his wife"). waiter("the waiter"). member("Karl", "Karl and his wife"). member("his wife", "Karl and his wife"). st_hpd(enter("Karl and his wife", "new restaurant"), true, 0). st_hpd(lead_to(w, "Karl and his wife", t), true, 1). st_hpd(order("Karl and his wife", f, "the waiter"), false). st_hpd(complain("Karl and his wife", "the waiter"), false). st_hpd(leave("Karl and his wife"), true, 2).
```

### Ground Truth
```clingo
restaurant("new restaurant"). waiter("the waiter"). customer(they). person("Karl"). person("his wife"). member("Karl", they). member("his wife", they). waiter(w). st_obs(sitting(they), true, 0). st_hpd(served(they), false, 1). st_hpd(leave(they), true, 2).
```

---

## Story #0 — Partial Match (Similarity: 0.2273)

**Story:** Allie enters the restaurant and claims her reservation. The waiter seats her at her table. She orders fruit salad. The waiter brings her fruit salad. After eating, she asks for the bill.

### Predicted
```clingo
restaurant("the restaurant"). customer("Allie"). person("Allie"). waiter("the waiter"). food("fruit salad"). st_hpd(enter("Allie", "the restaurant"), true, 0). st_hpd(greet("the waiter", "Allie"), true, 1). st_hpd(lead_to("the waiter", "Allie", t), true, 2). st_hpd(sit("Allie"), true, 3). st_hpd(order("Allie", "fruit salad", "the waiter"), true, 4). st_hpd(prepare(c, "fruit salad", "the waiter"), true, 5). st_obs(food_prepared(c, "fruit salad", "the waiter"), true, 5). st_hpd(move("the waiter", l1, t), true, 6). st_hpd(put_down("the waiter", "fruit salad", t), true, 6). st_obs(served("Allie"), true, 6). st_hpd(eat("Allie", "fruit salad"), true, 7). st_hpd(request("Allie", b, "the waiter"), true, 8).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer("Allie"). food("fruit salad"). waiter("the waiter"). story_step(0..6). st_hpd(enter("Allie", "the restaurant"), true, 0). st_hpd(lead_to("the waiter", "Allie", t), true, 1). st_hpd(sit("Allie"), true, 2). st_hpd(order("Allie", "fruit salad", "the waiter"), true, 3). st_hpd(put_down("the waiter", "fruit salad", t), true, 4). st_hpd(eat("Allie", "fruit salad"), true, 5). st_hpd(request("Allie", b, "the waiter"), true, 6).
```

---

## Story #96 — Partial Match (Similarity: 0.2273)

**Story:** [REDACTED — original ROCStories text; storyid=77710d2a-dbc2-4c99-a892-190b529ad219]

### Predicted
```clingo
restaurant("fast food restaurant"). customer("Dina"). customer("friend"). person("Dina"). person("friend"). food("fries"). st_obs(in("Dina", "fast food restaurant"), true, 0). st_obs(in("friend", "fast food restaurant"), true, 0). st_obs(hungry("Dina"), false, 0). st_hpd(order("Dina", "fries", w), true, 1). member("Dina", "group"). member("friend", "group"). member("fries", "order"). st_hpd(pay("Dina", b), true, 2). st_hpd(pay("friend", b), true, 2). st_hpd(eat("Dina", "fries"), true, 3).
```

### Ground Truth
```clingo
restaurant("fast food restaurant"). customer(they). person("Dina"). person("a friend"). member("Dina", they). member("a friend", they). food("fries"). st_obs(in("Dina", "fast food restaurant"), true, 0). st_obs(hungry("Dina"), false, 1). st_hpd(order(they, "fries", w), true, 2). st_hpd(pay("Dina", b), true, 3). st_hpd(pay("a friend", b), true, 3). st_hpd(eat("Dina", "fries"), true, 4).
```

---

## Story #29 — Partial Match (Similarity: 0.2353)

**Story:** Nicole went to a vegetarian restaurant. She ordered lentil soup. When the waitress brought her the soup, she told Nicole that it was on the house. Nicole enjoyed the soup and then left.

### Predicted
```clingo
restaurant("vegetarian restaurant"). customer("Nicole"). person("Nicole"). waiter("waitress"). food("lentil soup"). st_hpd(enter("Nicole", "vegetarian restaurant"), true, 0). st_hpd(order("Nicole", "lentil soup", "waitress"), true, 1). st_hpd(bring("waitress", "lentil soup", "Nicole"), true, 2). st_hpd(inform("waitress", "on the house", "Nicole"), true, 2). st_hpd(eat("Nicole", "lentil soup"), true, 3). st_hpd(leave("Nicole"), true, 4).
```

### Ground Truth
```clingo
restaurant(veg_r). customer(nicole). person(owner). food(lentil_soup). waiter(waitress). story_step(0..5). st_hpd(enter(nicole, veg_r), true, 0). st_hpd(order(nicole, lentil_soup, waitress), true, 1). st_hpd(pay(owner, b), true, 2). st_hpd(put_down(waitress, lentil_soup, t), true, 3). st_hpd(eat(nicole, lentil_soup), true, 4). st_hpd(leave(nicole), true, 5).
```

---

## Story #3 — Partial Match (Similarity: 0.2381)

**Story:** Jill enters the restaurant and is escorted to a table. She orders chicken. The waiter brings the chicken to her table. After eating, Jill asks for the bill.

### Predicted
```clingo
restaurant("the restaurant"). customer("Jill"). person("Jill"). waiter("the waiter"). food("chicken"). st_hpd(enter("Jill", "the restaurant"), true, 0). st_hpd(greet("the waiter", "Jill"), true, 1). st_hpd(lead_to("the waiter", "Jill", t), true, 2). st_hpd(sit("Jill"), true, 3). st_hpd(order("Jill", "chicken", "the waiter"), true, 4). st_hpd(prepare(c, "chicken", "the waiter"), true, 5). st_obs(food_prepared(c, "chicken", "the waiter"), true, 5). st_hpd(move("the waiter", l1, t), true, 6). st_hpd(put_down("the waiter", "chicken", t), true, 6). st_obs(served("Jill"), true, 6). st_hpd(eat("Jill", "chicken"), true, 7). st_hpd(request("Jill", b, "the waiter"), true, 8).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer("Jill"). food("chicken"). waiter("the waiter"). story_step(0..5). st_hpd(enter("Jill", "the restaurant"), true, 0). st_hpd(lead_to("the waiter", "Jill", t), true, 1). st_hpd(order("Jill", "chicken", "the waiter"), true, 2). st_hpd(put_down("the waiter", "chicken", t), true, 3). st_hpd(eat("Jill", "chicken"), true, 4). st_hpd(request("Jill", b, "the waiter"), true, 5).
```

---

## Story #57 — Partial Match (Similarity: 0.2381)

**Story:** Carlos arrived at the Mexican restaurant and was greeted warmly. He ordered tacos and a margarita. The food arrived quickly and was perfectly prepared. Carlos enjoyed his meal thoroughly.

### Predicted
```clingo
person("Carlos"). customer("Carlos"). food("tacos"). beverage("margarita"). restaurant("Mexican restaurant"). st_hpd(enter("Carlos", "Mexican restaurant"), true, 0). st_hpd(greet("the host", "Carlos"), true, 1). st_hpd(order("Carlos", "tacos", "the waiter"), true, 2). st_hpd(order("Carlos", "margarita", "the waiter"), true, 2). st_hpd(eat("Carlos", "tacos"), true, 3). st_hpd(drink("Carlos", "margarita"), true, 3). st_obs(in("Carlos", "Mexican restaurant"), true, 0). st_obs(welcomed("Carlos"), true, 1). st_obs(served("Carlos"), true, 3).
```

### Ground Truth
```clingo
restaurant("Mexican restaurant"). customer("Carlos"). waiter(w). food("tacos"). beverage("margarita"). story_step(0..4). st_hpd(enter("Carlos", "Mexican restaurant"), true, 0). st_hpd(greet(w, "Carlos"), true, 1). st_hpd(order("Carlos", "tacos", w), true, 2). st_hpd(order("Carlos", "margarita", w), true, 2). st_hpd(put_down(w, "tacos", t), true, 3). st_hpd(put_down(w, "margarita", t), true, 3). st_hpd(eat("Carlos", "tacos"), true, 4). st_hpd(drink("Carlos", "margarita"), true, 4).
```

---

## Story #42 — Partial Match (Similarity: 0.2400)

**Story:** David and his date, Sarah, went to a fancy restaurant. David ordered for both of them, choosing the duck confit. The waiter served the meal and poured them some wine. They enjoyed their dinner.

### Predicted
```clingo
restaurant("fancy restaurant"). customer("David"). customer("Sarah"). person("David"). person("Sarah"). food("duck confit"). beverage("wine"). waiter("the waiter"). member("David", "group"). member("Sarah", "group"). member("duck confit", f). st_obs(in("David", "fancy restaurant"), true, 0). st_obs(in("Sarah", "fancy restaurant"), true, 0). st_hpd(order_for("David", "Sarah", "duck confit", "the waiter"), true, 1). st_hpd(prepare("cook", "duck confit", "the waiter"), true, 2). st_hpd(eat("David", "duck confit"), true, 3). st_hpd(eat("Sarah", "duck confit"), true, 3). st_hpd(drink("David", "wine"), true, 4). st_hpd(drink("Sarah", "wine"), true, 4).
```

### Ground Truth
```clingo
restaurant("fancy restaurant"). customer(they). person("David"). person("Sarah"). member("David", they). member("Sarah", they). food("duck confit"). beverage("wine"). waiter("the waiter"). story_step(0..3). st_hpd(order_for("David", they, "duck confit", "the waiter"), true, 0). st_hpd(put_down("the waiter", "duck confit", t), true, 1). st_hpd(put_down("the waiter", "wine", t), true, 2). st_hpd(eat(they, "duck confit"), true, 3). st_hpd(drink(they, "wine"), true, 3).
```

---

## Story #71 — Partial Match (Similarity: 0.2400)

**Story:** Michael entered the bistro and was led to a table by a waitress. He ordered the daily special and a glass of water. The waitress brought his meal promptly. Michael enjoyed his food and asked for the check.

### Predicted
```clingo
restaurant("bistro"). customer("Michael"). person("Michael"). waiter("waitress"). food("daily special"). beverage("glass of water"). st_hpd(enter("Michael", "bistro"), true, 0). st_hpd(lead_to("waitress", "Michael", t), true, 1). st_hpd(order("Michael", "daily special", "waitress"), true, 2). st_hpd(order("Michael", "glass of water", "waitress"), true, 3). st_hpd(move("waitress", w, t), true, 4). st_obs(holding("waitress", "daily special"), true, 4). st_obs(holding("waitress", "glass of water"), true, 4). st_hpd(put_down("waitress", "daily special", t), true, 5). st_hpd(put_down("waitress", "glass of water"), t), true, 5). st_hpd(eat("Michael", "daily special"), true, 6). st_hpd(drink("Michael", "glass of water"), true, 6). st_hpd(request("Michael", b, "waitress"), true, 7).
```

### Ground Truth
```clingo
restaurant("the bistro"). customer("Michael"). food("daily special"). beverage("water"). waiter("the waitress"). st_hpd(enter("Michael", "the bistro"), true, 0). st_hpd(lead_to("the host", "Michael", t), true, 1). st_hpd(order("Michael", "daily special", "the waitress"), true, 2). st_hpd(order("Michael", "water", "the waitress"), true, 2). st_hpd(put_down("the waitress", "daily special", t), true, 3). st_hpd(put_down("the waitress", "water", t), true, 3). st_hpd(eat("Michael", "daily special"), true, 4). st_hpd(drink("Michael", "water"), true, 4). st_hpd(request("Michael", b, "the waitress"), true, 5).
```

---

## Story #80 — Partial Match (Similarity: 0.2400)

**Story:** [REDACTED — original ROCStories text; storyid=d85b7ce5-0d84-4181-afe4-52c64711145a]

### Predicted
```clingo
restaurant("Genki Ya"). customer("my son"). customer("I"). person("my son"). person("I"). food("fish roe"). food("combo sashimi-sushi dish"). beverage("Japanese beer"). member("my son", "we"). member("I", "we"). member("Japanese beer", "drinks"). member("fish roe", "food order"). member("combo sashimi-sushi dish", "food order"). st_hpd(enter("we", "Genki Ya"), true, 0). st_obs(in("we", "Genki Ya"), true, 0). st_hpd(order("we", "drinks", w), true, 1). st_hpd(order("we", "food order", w), true, 2). st_hpd(eat("we", "food order"), true, 3). st_hpd(drink("we", "drinks"), true, 4). st_hpd(leave("we"), true, 5).
```

### Ground Truth
```clingo
restaurant("Genki Ya"). customer(we). person("my son"). person("I"). member("my son", we). member("I", we). beverage("japanese beers"). food(f). member("fish roe", f). member("sashimi-sushi dishes", f). st_hpd(enter(we, "Genki Ya"), true, 0). st_hpd(eat(we, f), true, 2). st_hpd(drink(we, "japanese beers"), true, 2).
```

---

## Story #40 — Partial Match (Similarity: 0.2500)

**Story:** Ken was at a sushi restaurant. He ordered the tuna roll. The waiter brought the tuna roll, but Ken noticed a long hair in it. He complained to the waiter, who apologized and brought a new, hair-free roll.

### Predicted
```clingo
restaurant("sushi restaurant"). customer("Ken"). person("Ken"). food("tuna roll"). waiter("the waiter"). st_obs(in("Ken", "sushi restaurant"), true, 0). st_hpd(order("Ken", "tuna roll", "the waiter"), true, 1). st_hpd(prepare("cook", "tuna roll", "the waiter"), true, 2). st_hpd(complain("Ken", "the waiter"), true, 3). st_hpd(prepare("cook", "tuna roll", "the waiter"), true, 4). st_hpd(eat("Ken", "tuna roll"), true, 5).
```

### Ground Truth
```clingo
restaurant("sushi restaurant"). customer("Ken"). food("tuna roll"). food("new tuna roll"). waiter("the waiter"). story_step(0..4). st_hpd(order("Ken", "tuna roll", "the waiter"), true, 0). st_hpd(put_down("the waiter", "tuna roll", t), true, 1). st_hpd(complain("Ken", "the waiter"), true, 2). st_next(1, 2). st_hpd(put_down(w, "new tuna roll", t), true, 3).
```

---

## Story #66 — Partial Match (Similarity: 0.2500)

**Story:** Charlie entered a restaurant and was led to a table. He ordered a burger. The waiter brought the burger. Charlie ate it, asked for the bill, paid, and left.

### Predicted
```clingo
person("Charlie"). customer("Charlie"). waiter("the waiter"). restaurant("a restaurant"). food("burger"). st_hpd(enter("Charlie", "a restaurant"), true, 0). st_hpd(lead_to(w, "Charlie", t), true, 1). st_hpd(sit("Charlie"), true, 2). st_hpd(order("Charlie", "burger", "the waiter"), true, 3). st_obs(served("Charlie"), true, 4). st_hpd(eat("Charlie", "burger"), true, 5). st_hpd(request("Charlie", b, "the waiter"), true, 6). st_hpd(pay("Charlie", b), true, 7). st_hpd(leave("Charlie"), true, 8).
```

### Ground Truth
```clingo
restaurant("a restaurant"). customer("Charlie"). food("burger"). waiter("the waiter"). story_step(0..7). st_hpd(enter("Charlie", "a restaurant"), true, 0). st_hpd(lead_to("the waiter", "Charlie", t), true, 1). st_hpd(order("Charlie", "burger", "the waiter"), true, 2). st_hpd(put_down("the waiter", "burger", t), true, 3). st_hpd(eat("Charlie", "burger"), true, 4). st_hpd(request("Charlie", b, "the waiter"), true, 5). st_hpd(pay("Charlie", b), true, 6). st_hpd(leave("Charlie"), true, 7).
```

---

## Story #88 — Partial Match (Similarity: 0.2500)

**Story:** [REDACTED — original ROCStories text; storyid=3a66621b-9dcf-4e32-b085-e4c0a2e89f8f]

### Predicted
```clingo
restaurant("this little deli"). customer("I"). person("I"). food("turkey sandwich"). st_obs(hungry("I"), true, 0). st_hpd(enter("I", "this little deli"), true, 1). st_obs(in("I", "this little deli"), true, 1). st_hpd(order("I", "turkey sandwich", w), true, 2). st_hpd(eat("I", "turkey sandwich"), true, 3). st_hpd(leave("I"), true, 4).
```

### Ground Truth
```clingo
restaurant("little deli"). customer("I"). food("turkey sandwich"). st_obs(hungry("I"), true, 0). st_hpd(order("I", "turkey sandwich", w), true, 1). st_hpd(eat("I", "turkey sandwich"), true, 2).
```

---

## Story #95 — Partial Match (Similarity: 0.2500)

**Story:** [REDACTED — original ROCStories text; storyid=cd9a0a7b-ef8f-42c0-86ac-fe80542cebd3]

### Predicted
```clingo
restaurant(r). person("Austin"). waiter("Austin"). customer("homeless man"). person("homeless man"). food("spare food"). food("full meal"). st_hpd(enter("homeless man", r), true, 0). st_hpd(request("homeless man", "spare food", "Austin"), true, 1). st_hpd(lead_to("Austin", "homeless man", t), true, 2). st_hpd(sit("homeless man"), true, 3). st_hpd(order("Austin", "full meal", "Austin"), true, 4). st_hpd(prepare("cook", "full meal", "Austin"), true, 5). st_obs(food_prepared("cook", "full meal", "Austin"), true, 6). st_hpd(eat("homeless man", "full meal"), true, 7).
```

### Ground Truth
```clingo
restaurant("a restaurant"). customer("a homeless man"). waiter("wait staff"). person("Austin"). food("spare food"). food("full meal").  st_hpd(enter("a homeless man", "a restaurant"), true, 0). st_hpd(request("a homeless man", "spare food", "Austin"), true, 1). st_hpd(sit("a homeless man"), true, 2). st_hpd(put_down("wait staff", "full meal", t), true, 3). st_hpd(pay("a homeless man", b), false).
```

---

## Story #41 — Partial Match (Similarity: 0.2632)

**Story:** Laura was at a cafe. She ordered a coffee and a croissant. The waiter brought the coffee promptly, but after 30 minutes, the croissant still hadn't arrived. Laura gave up, paid for her coffee, and left.

### Predicted
```clingo
restaurant("cafe"). customer("Laura"). person("Laura"). beverage("coffee"). food("croissant"). waiter("the waiter"). st_obs(in("Laura", "cafe"), true, 0). st_hpd(order("Laura", "coffee", "the waiter"), true, 1). st_hpd(order("Laura", "croissant", "the waiter"), true, 2). st_hpd(prepare("cook", "coffee", "the waiter"), true, 3). st_hpd(drink("Laura", "coffee"), true, 4). st_hpd(prepare("cook", "croissant", "the waiter"), false). st_hpd(pay("Laura", b), true, 5). st_hpd(leave("Laura"), true, 6).
```

### Ground Truth
```clingo
restaurant("cafe"). customer("Laura"). beverage("coffee"). food("croissant").  waiter("the waiter"). story_step(0..4). st_hpd(order("Laura", "coffee", "the waiter"), true, 0). st_hpd(order("Laura", "croissant", "the waiter"), true, 0). st_hpd(put_down("the waiter", "coffee", t), true, 1). st_obs(served("Laura"), false, 2). st_hpd(pay("Laura", b), true, 3). st_hpd(leave("Laura"), true, 4).
```

---

## Story #7 — Partial Match (Similarity: 0.2667)

**Story:** Larry is seated at his table in the restaurant. The waiter brings him a menu so he can decide what to order. After reviewing the menu, Larry decides he doesn't want anything at this restaurant.

### Predicted
```clingo
restaurant("the restaurant"). customer("Larry"). person("Larry"). waiter("the waiter"). st_obs(sitting("Larry"), true, 0). st_obs(at_l("Larry", t), true, 0). st_hpd(move("the waiter", l1, t), true, 1). st_hpd(put_down("the waiter", "menu", t), true, 1). st_hpd(pick_up("Larry", "menu", t), true, 2). st_hpd(read_menu("Larry"), true, 3). st_obs(menu_read("Larry"), true, 3). st_hpd(put_down("Larry", "menu", t), true, 4). st_hpd(order("Larry"), false).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer("Larry"). waiter("the waiter"). story_step(0..3). st_obs(sitting("Larry"), true, 0). st_hpd(put_down("the waiter", m, t), true, 1). st_obs(menu_read("Larry"), true, 2). st_hpd(order("Larry"), false, 3).
```

---

## Story #63 — Partial Match (Similarity: 0.2667)

**Story:** At a cafe, Ivan ordered an espresso. The waiter brought it to his table. Ivan drank the espresso, left cash on the table for the bill, and then departed.

### Predicted
```clingo
person("Ivan"). customer("Ivan"). waiter("the waiter"). restaurant("a cafe"). beverage("espresso"). st_hpd(enter("Ivan", "a cafe"), true, 0). st_hpd(order("Ivan", "espresso", "the waiter"), true, 1). st_obs(served("Ivan"), true, 2). st_hpd(drink("Ivan", "espresso"), true, 3). st_hpd(pay("Ivan", b), true, 4). st_hpd(leave("Ivan"), true, 5).
```

### Ground Truth
```clingo
restaurant("cafe"). customer("Ivan"). beverage("espresso"). waiter("the waiter"). story_step(0..4). st_hpd(order("Ivan", "espresso", "the waiter"), true, 0). st_hpd(put_down("the waiter", "espresso", t), true, 1). st_hpd(drink("Ivan", "espresso"), true, 2). st_hpd(pay("Ivan", b), true, 3). st_hpd(leave("Ivan"), true, 4).
```

---

## Story #31 — Partial Match (Similarity: 0.2778)

**Story:** Nicole went to a vegetarian restaurant. She ordered lentil soup. The waitress brought her a miso soup instead. Nicole decided to eat it anyway.

### Predicted
```clingo
restaurant("vegetarian restaurant"). customer("Nicole"). person("Nicole"). food("lentil soup"). food("miso soup"). waiter("the waitress"). st_obs(in("Nicole", "vegetarian restaurant"), true, 0). st_hpd(order("Nicole", "lentil soup", "the waitress"), true, 1). st_hpd(prepare(cook, "miso soup", "the waitress"), true, 2). st_obs(food_prepared(cook, "miso soup", "the waitress"), true, 2). st_hpd(eat("Nicole", "miso soup"), true, 3). st_hpd(complain("Nicole", "the waitress"), false).
```

### Ground Truth
```clingo
restaurant(veg_r). customer(nicole). person(owner). food(lentil_soup). food(miso_soup). waiter(waitress). story_step(0..4). st_hpd(enter(nicole, veg_r), true, 0). st_hpd(order(nicole, lentil_soup, waitress), true, 1). st_hpd(put_down(waitress, miso_soup, t), true, 2). stop_activity(nicole, 3). next_st(2, 3). st_hpd(eat(nicole, miso_soup), true, 4).
```

---

## Story #56 — Partial Match (Similarity: 0.2778)

**Story:** Anna visited the vegan restaurant downtown. She ordered the quinoa bowl and a green smoothie. The food was fresh and delicious. She left a generous tip for the excellent service.

### Predicted
```clingo
person("Anna"). customer("Anna"). food("quinoa bowl"). beverage("green smoothie"). restaurant("vegan restaurant"). st_hpd(enter("Anna", "vegan restaurant"), true, 0). st_hpd(order("Anna", "quinoa bowl", "the waiter"), true, 1). st_hpd(order("Anna", "green smoothie", "the waiter"), true, 1). st_hpd(eat("Anna", "quinoa bowl"), true, 2). st_hpd(drink("Anna", "green smoothie"), true, 2). st_hpd(pay("Anna", tip), true, 3). st_obs(in("Anna", "vegan restaurant"), true, 0). st_obs(served("Anna"), true, 2).
```

### Ground Truth
```clingo
restaurant("vegan restaurant"). customer("Anna"). food("quinoa bowl"). beverage("green smoothie"). waiter(w). story_step(0..4). st_hpd(enter("Anna", "vegan restaurant"), true, 0). st_hpd(order("Anna", "quinoa bowl", w), true, 1). st_hpd(order("Anna", "green smoothie", w), true, 1). st_hpd(eat("Anna", "quinoa bowl"), true, 3). st_hpd(drink("Anna", "green smoothie"), true, 3). st_hpd(pay("Anna", tip), true, 4).
```

---

## Story #65 — Partial Match (Similarity: 0.2800)

**Story:** Maria entered the Italian restaurant and was greeted by the host. She was seated at a corner table and handed a menu. Maria ordered spaghetti carbonara and a glass of red wine. The waiter brought her order promptly. She enjoyed her meal and asked for the bill.

### Predicted
```clingo
person("Maria"). customer("Maria"). host("the host"). waiter("the waiter"). restaurant("the Italian restaurant"). food("spaghetti carbonara"). beverage("red wine"). st_hpd(enter("Maria", "the Italian restaurant"), true, 0). st_hpd(greet("the host", "Maria"), true, 1). st_hpd(lead_to("the host", "Maria", "corner table"), true, 2). st_hpd(sit("Maria"), true, 3). st_hpd(order("Maria", "spaghetti carbonara", "the waiter"), true, 4). st_hpd(order("Maria", "red wine", "the waiter"), true, 4). st_obs(served("Maria"), true, 5). st_hpd(eat("Maria", "spaghetti carbonara"), true, 6). st_hpd(drink("Maria", "red wine"), true, 6). st_hpd(request("Maria", b, "the waiter"), true, 7).
```

### Ground Truth
```clingo
restaurant("Italian restaurant"). customer("Maria"). person("the host"). food("spaghetti carbonara"). beverage("red wine"). waiter("the waiter"). story_step(0..6). st_hpd(enter("Maria", "Italian restaurant"), true, 0). st_hpd(greet("the host", "Maria"), true, 1). st_hpd(lead_to("the host", "Maria", t), true, 2). st_hpd(order("Maria", "spaghetti carbonara", "the waiter"), true, 3). st_hpd(order("Maria", "red wine", "the waiter"), true, 3). st_hpd(put_down("the waiter", "spaghetti carbonara", t), true, 4). st_hpd(put_down("the waiter", "red wine", t), true, 4). st_hpd(eat("Maria", "spaghetti carbonara"), true, 5). st_hpd(drink("Maria", "red wine"), true, 5). st_hpd(request("Maria", b, "the waiter"), true, 6).
```

---

## Story #82 — Partial Match (Similarity: 0.2800)

**Story:** [REDACTED — original ROCStories text; storyid=2cf524c3-5e49-4ba9-9590-f84429fbdc01]

### Predicted
```clingo
restaurant("new restaurant"). customer("Elmer"). customer("Emma"). person("Elmer"). person("Emma"). food("burger"). food("fries"). beverage("milkshake"). member("Elmer", "the couple"). member("Emma", "the couple"). member("burger", "food order"). member("milkshake", "drink order"). st_hpd(enter("the couple", "new restaurant"), true, 0). st_obs(in("the couple", "new restaurant"), true, 0). st_hpd(order("the couple", "food order", w), true, 1). st_hpd(order("the couple", "drink order", w), true, 2). st_hpd(order("Elmer", "fries", w), true, 3). st_hpd(eat("the couple", "food order"), true, 4). st_hpd(eat("the couple", "fries"), true, 5). st_hpd(drink("the couple", "drink order"), true, 6). st_hpd(leave("the couple"), true, 7).
```

### Ground Truth
```clingo
restaurant("new restaurant"). customer("the couple"). person("Elmer"). person("Emma"). member("Elmer", "the couple"). member("Emma", "the couple"). food("burgers"). food("fries"). beverage("milkshakes"). st_hpd(enter("the couple", "new restaurant"), true, 0). st_hpd(order("the couple", "burgers", w), true, 1). st_hpd(order("the couple", "milkshakes", w), true, 1). st_hpd(order("Elmer", "fries", w), true, 2).
```

---

## Story #23 — Partial Match (Similarity: 0.2917)

**Story:** I opened the menu and chose the salmon. The waiter poured two glasses of red wine. I sipped the wine. Then our server brought a small plate of hors d'oeuvres. I tried a little bit of everything. Soon, the waiter brought the meal. I tasted the salmon.

### Predicted
```clingo
restaurant(r). customer("I"). person("I"). waiter("the waiter"). waiter("our server"). food("salmon"). food("a small plate of hors d'oeuvres"). food("the meal"). beverage("red wine"). st_hpd(open_menu("I"), true, 0). st_hpd(choose("I", "salmon"), true, 1). st_hpd(pour("the waiter", "red wine", "I"), true, 2). st_hpd(pour("the waiter", "red wine", "companion"), true, 2). st_hpd(drink("I", "red wine"), true, 3). st_hpd(bring("our server", "a small plate of hors d'oeuvres", "table"), true, 4). st_hpd(eat("I", "a small plate of hors d'oeuvres"), true, 5). st_hpd(bring("the waiter", "the meal", "table"), true, 6). st_hpd(eat("I", "salmon"), true, 7).
```

### Ground Truth
```clingo
restaurant(r). customer("I"). food(salmon). beverage("red wine"). food("hors d'oeuvres"). waiter("the waiter"). story_step(0..7). st_hpd(pick_up("I", m, t), true, 0). st_hpd(order("I", salmon, "the waiter"), true, 1). st_hpd(put_down("I", "red wine", t), true, 2). st_hpd(drink("I", "red wine"), true, 3). st_hpd(put_down("the waiter", "hors d'oeuvres", t), true, 4). st_hpd(eat("I", "hors d'oeuvres"), true, 5). st_hpd(put_down("the waiter", salmon, t), true, 6). st_hpd(eat("I", salmon), true, 7).
```

---

## Story #25 — Partial Match (Similarity: 0.2941)

**Story:** I was the first person to appear at the restaurant. I took my seat at the middle of the table. The head-waiter waited on me himself. I had a capital dinner. Then Uncle Chipperton entered. He paid for the whole dinner.

### Predicted
```clingo
restaurant(r). customer("I"). customer("Uncle Chipperton"). person("I"). person("Uncle Chipperton"). waiter("head-waiter"). food("dinner"). st_hpd(enter("I", r), true, 0). st_hpd(sit("I"), true, 1). st_hpd(serve("head-waiter", "I"), true, 2). st_hpd(eat("I", "dinner"), true, 3). st_hpd(enter("Uncle Chipperton", r), true, 4). st_hpd(pay("Uncle Chipperton", b), true, 5).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer("I"). waiter("head-waiter") food("capital dinner"). person("Uncle Chipperton"). story_step(0..5). st_hpd(enter("I", "the restaurant"), true, 0). st_hpd(sit("I"), true, 1). st_hpd(put_down("head-waiter", "capital dinner", t), true, 2). st_hpd(eat("I", "capital dinner"), true, 3). st_hpd(enter("Uncle Chipperton", "the restaurant"), true, 4). st_hpd(pay("Uncle Chipperton", b), true, 5).
```

---

## Story #9 — Partial Match (Similarity: 0.3000)

**Story:** Pete is seated at his table in the restaurant. He has ordered and received his chicken, but is unhappy with how undercooked the chicken is. He complains to the waiter, and asks for a better cooked dish.

### Predicted
```clingo
restaurant("the restaurant"). customer("Pete"). person("Pete"). waiter("the waiter"). food("chicken"). st_obs(sitting("Pete"), true, 0). st_obs(at_l("Pete", t), true, 0). st_hpd(order("Pete", "chicken", "the waiter"), true, 1). st_hpd(prepare(c, "chicken", "the waiter"), true, 2). st_obs(food_prepared(c, "chicken", "the waiter"), true, 2). st_hpd(move("the waiter", l1, t), true, 3). st_hpd(put_down("the waiter", "chicken", t), true, 3). st_obs(served("Pete"), true, 3). st_hpd(complain("Pete", "the waiter"), true, 4). st_hpd(request("Pete", "a better cooked dish", "the waiter"), true, 5).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer("Pete"). food("chicken"). food("undercooked chicken"). food("better cooked chicken"). waiter("the waiter"). story_step(0..4). st_obs(sitting("Pete"), true, 0). st_hpd(order("Pete", "chicken", "the waiter"), true, 1). st_hpd(put_down("the waiter", "undercooked_chicken", t), true, 2). st_hpd(complain("Pete", "the waiter"), true, 3). st_next(2, 3). st_hpd(order("Pete", "better cooked chicken", "the waiter"), true, 4).
```

---

## Story #10 — Partial Match (Similarity: 0.3077)

**Story:** Jim is seated at his table in the restaurant. He orders an appetizer. After waiting for 20 minutes and not receiving his food, he decides to leave the restaurant.

### Predicted
```clingo
restaurant("the restaurant"). customer("Jim"). person("Jim"). food("appetizer"). waiter("the waiter"). st_obs(sitting("Jim"), true, 0). st_obs(at_l("Jim", t), true, 0). st_obs(in("Jim", "the restaurant"), true, 0). st_hpd(order("Jim", "appetizer", "the waiter"), true, 1). st_hpd(leave("Jim"), true, 2). st_obs(served("Jim"), false, 1).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer("Jim"). food("appetizer"). story_step(0..3). st_obs(sitting("Jim"), true, 0). st_hpd(order("Jim", "appetizer", w), true, 1). st_obs(served("Pete"), false, 2). st_hpd(leave("Jim"), true, 3).
```

---

## Story #46 — Partial Match (Similarity: 0.3077)

**Story:** Rita finished her salad. She requested the bill from the waiter. The waiter brought the bill, and Rita paid with her credit card.

### Predicted
```clingo
restaurant(r). customer("Rita"). person("Rita"). food("salad"). waiter("the waiter"). st_obs(in("Rita", r), true, 0). st_hpd(eat("Rita", "salad"), true, 1). st_hpd(request("Rita", b, "the waiter"), true, 2). st_hpd(read_bill("Rita"), true, 3). st_hpd(pay("Rita", b), true, 4).
```

### Ground Truth
```clingo
restaurant(r). customer("Rita"). food("salad"). waiter("the waiter"). story_step(0..3). st_hpd(eat("Rita", "salad"), true, 0). st_hpd(request("Rita", b, "the waiter"), true, 1). st_hpd(put_down("the waiter", b, t), true, 2). st_hpd(pay("Rita", b), true, 3).
```

---

## Story #85 — Partial Match (Similarity: 0.3077)

**Story:** [REDACTED — original ROCStories text; storyid=9915e783-6bf9-4d92-9150-b031bf778bb7]

### Predicted
```clingo
restaurant(r). customer("I"). person("I"). food("pizza"). st_hpd(enter("I", r), true, 0). st_obs(in("I", r), true, 0). st_hpd(order("I", "pizza", w), true, 1). st_hpd(complain("I", w), true, 2). st_hpd(leave("I"), true, 3). st_hpd(eat("I", "pizza"), false).
```

### Ground Truth
```clingo
restaurant("a restaurant"). customer("I"). food("pizza"). food("burnt pizza"). st_hpd(enter("I", r), true, 0). st_hpd(order("I", "pizza", w), true, 1). st_hpd(put_down(w, "burnt pizza", t), true, 2). st_hpd(request("I", pick_up(w, "burnt pizza", t), w), true, 3).
```

---

## Story #8 — Partial Match (Similarity: 0.3125)

**Story:** Derek ordered a vegetable soup. The waiter brought out the vegetable soup, but Derek was unsatisfied with the lack of vegetables in it. As an apology, the waiter decided not to charge Derek for the soup.

### Predicted
```clingo
restaurant("the restaurant"). customer("Derek"). person("Derek"). waiter("the waiter"). food("vegetable soup"). st_hpd(order("Derek", "vegetable soup", "the waiter"), true, 0). st_hpd(prepare(c, "vegetable soup", "the waiter"), true, 1). st_obs(food_prepared(c, "vegetable soup", "the waiter"), true, 1). st_hpd(move("the waiter", l1, t), true, 2). st_hpd(put_down("the waiter", "vegetable soup", t), true, 2). st_obs(served("Derek"), true, 2). st_hpd(complain("Derek", "the waiter"), true, 3). st_hpd(cancel_bill("the waiter"), true, 4).
```

### Ground Truth
```clingo
restaurant("restaurant"). customer("Derek"). food("vegetable soup"). waiter("the waiter"). story_step(0..3). st_hpd(order("Derek", "vegetable soup", "the waiter"), true, 0). st_hpd(put_down("the waiter", "vegetable soup", t), true, 1). st_hpd(complain("Derek", "the waiter"), true, 2). st_next(1, 2). st_hpd(pay("derek", b), false, 3).
```

---

## Story #76 — Partial Match (Similarity: 0.3158)

**Story:** [REDACTED — original ROCStories text; storyid=6ead4a09-8e5f-4fbc-8a32-b706bdbb7a87]

### Predicted
```clingo
restaurant("Allston Diner"). customer("we"). customer("our son"). customer("friend"). person("we"). person("our son"). person("friend"). food("large, hearty breakfast meals"). member("we", "we"). member("our son", "we"). member("friend", "we"). st_hpd(enter("we", "Allston Diner"), true, 0). st_hpd(enter("friend", "Allston Diner"), true, 1). st_hpd(order("we", "large, hearty breakfast meals", w), true, 2). st_hpd(move(w, w, t), true, 3). st_obs(holding(w, "large, hearty breakfast meals"), true, 3). st_hpd(put_down(w, "large, hearty breakfast meals", t), true, 4). st_hpd(eat("we", "large, hearty breakfast meals"), true, 5). st_hpd(eat("friend", "large, hearty breakfast meals"), true, 5).
```

### Ground Truth
```clingo
restaurant("Allston Diner"). customer(we). person("our son"). customer("a friend"). member("our son", we). food("breakfast meals"). st_hpd(enter(we, "Allston Diner"), true, 0). st_hpd(eat(we, "breakfast meals"), true, 1). st_hpd(eat("a friend", "breakfast meals"), true, 1).
```

---

## Story #1 — Partial Match (Similarity: 0.3333)

**Story:** Abdul is sitting in a vegetarian restaurant. The waiter takes his order, and he orders hummus. The waiter brings the hummus to the table.

### Predicted
```clingo
restaurant("a vegetarian restaurant"). customer("Abdul"). person("Abdul"). waiter("the waiter"). food("hummus"). st_obs(sitting("Abdul"), true, 0). st_obs(in("Abdul", "a vegetarian restaurant"), true, 0). st_hpd(greet("the waiter", "Abdul"), true, 1). st_hpd(order("Abdul", "hummus", "the waiter"), true, 2). st_hpd(prepare(c, "hummus", "the waiter"), true, 3). st_obs(food_prepared(c, "hummus", "the waiter"), true, 3). st_hpd(move("the waiter", l1, t), true, 4). st_hpd(put_down("the waiter", "hummus", t), true, 4). st_obs(served("Abdul"), true, 4).
```

### Ground Truth
```clingo
restaurant("vegetarian restaurant"). customer("Abdul"). food("hummus"). waiter("the waiter"). story_step(0..2). st_obs(sitting("Abdul"), true, 0). st_hpd(order("Abdul", "hummus", "the waiter"), true, 1). st_hpd(put_down("the waiter", "hummus", t), true, 2).
```

---

## Story #86 — Partial Match (Similarity: 0.3333)

**Story:** [REDACTED — original ROCStories text; storyid=541efb12-b331-4525-afe1-5422ff33a1ca]

### Predicted
```clingo
restaurant("a diner"). customer("Samuel"). customer("John"). person("Samuel"). person("John"). waiter("the waiter"). food("hamburger"). food("hotdog"). st_hpd(enter("Samuel", "a diner"), true, 0). st_hpd(enter("John", "a diner"), true, 0). st_obs(in("Samuel", "a diner"), true, 0). st_obs(in("John", "a diner"), true, 0). st_hpd(order("Samuel", "hamburger", "the waiter"), true, 1). st_hpd(complain("Samuel", "the waiter"), true, 2). st_hpd(order("the waiter", "hotdog", "the waiter"), true, 3). st_hpd(order("the waiter", "hamburger", "the waiter"), true, 4). st_hpd(eat("Samuel", "hamburger"), true, 5).
```

### Ground Truth
```clingo
restaurant("diner"). customer("Samuel"). customer("John"). food("hamburger without onions"). food("hotdog"). waiter("the waiter"). st_obs(in("Samuel", "diner"), true, 0). st_obs(in("John", "diner"), true, 0). st_hpd(order("Samuel", "hamburger without onions", "the waiter"), true, 1). st_hpd(put_down("the waiter", "hotdog", t), true, 2). st_hpd(complain("Samuel", "the waiter"), true, 3). st_next(2,3). st_hpd(put_down("the waiter", "hamburger without onions", t), true, 4).
```

---

## Story #72 — Partial Match (Similarity: 0.3500)

**Story:** Susan visited the pancake house for breakfast. She ordered blueberry pancakes and orange juice. The server brought her order quickly. Susan ate her breakfast and paid with her credit card.

### Predicted
```clingo
restaurant("pancake house"). customer("Susan"). person("Susan"). waiter("server"). food("blueberry pancakes"). beverage("orange juice"). st_hpd(enter("Susan", "pancake house"), true, 0). st_hpd(order("Susan", "blueberry pancakes", "server"), true, 1). st_hpd(order("Susan", "orange juice", "server"), true, 2). st_hpd(move("server", w, t), true, 3). st_obs(holding("server", "blueberry pancakes"), true, 3). st_obs(holding("server", "orange juice"), true, 3). st_hpd(put_down("server", "blueberry pancakes", t), true, 4). st_hpd(put_down("server", "orange juice", t), true, 4). st_hpd(eat("Susan", "blueberry pancakes"), true, 5). st_hpd(drink("Susan", "orange juice"), true, 5). st_hpd(pay("Susan", b), true, 6).
```

### Ground Truth
```clingo
restaurant("the pancake house"). customer("Susan"). food("blueberry pancakes"). beverage("orange juice"). waiter("the server"). st_hpd(enter("Susan", "the pancake house"), true, 0). st_hpd(order("Susan", "blueberry pancakes", "the server"), true, 1). st_hpd(order("Susan", "orange juice", "the server"), true, 1). st_hpd(put_down("the server", "blueberry pancakes", t), true, 2). st_hpd(eat("Susan", "blueberry pancakes"), true, 3). st_hpd(pay("Susan", b), true, 4).
```

---

## Story #58 — Partial Match (Similarity: 0.3529)

**Story:** Ben went to the diner for breakfast. He sat at the counter and ordered pancakes with bacon and coffee. The cook prepared his order right in front of him.

### Predicted
```clingo
person("Ben"). customer("Ben"). cook("the cook"). food("pancakes with bacon"). beverage("coffee"). restaurant("diner"). st_hpd(enter("Ben", "diner"), true, 0). st_hpd(sit("Ben"), true, 1). st_hpd(order("Ben", "pancakes with bacon", "the waiter"), true, 2). st_hpd(order("Ben", "coffee", "the waiter"), true, 2). st_hpd(prepare("the cook", "pancakes with bacon", "the waiter"), true, 3). st_obs(in("Ben", "diner"), true, 0). st_obs(at_l("Ben", "counter"), true, 1). st_obs(sitting("Ben"), true, 1). st_obs(food_prepared("the cook", "pancakes with bacon", "the waiter"), true, 3).
```

### Ground Truth
```clingo
restaurant("the diner"). customer("Ben"). food("pancakes with bacon"). beverage("coffee"). story_step(0..3). st_hpd(enter("Ben", "the diner"), true, 0). st_hpd(sit("Ben"), true, 1). st_hpd(order("Ben", "pancakes with bacon", w), true, 2). st_hpd(prepare("the cook", "pancakes with bacon", w), true, 3). st_hpd(prepare("the cook", "coffee", "Ben"), true, 3).
```

---

## Story #30 — Partial Match (Similarity: 0.3571)

**Story:** Nicole went to a vegetarian restaurant. She ordered lentil soup. The waitress brought her a miso soup instead.

### Predicted
```clingo
restaurant("vegetarian restaurant"). customer("Nicole"). person("Nicole"). food("lentil soup"). food("miso soup"). waiter("the waitress"). st_obs(in("Nicole", "vegetarian restaurant"), true, 0). st_hpd(order("Nicole", "lentil soup", "the waitress"), true, 1). st_hpd(prepare(cook, "miso soup", "the waitress"), true, 2). st_obs(food_prepared(cook, "miso soup", "the waitress"), true, 2). st_hpd(complain("Nicole", "the waitress"), false).
```

### Ground Truth
```clingo
restaurant(veg_r). customer(nicole). person(owner). food(lentil_soup). food(miso_soup). waiter(waitress). story_step(0..2). st_hpd(enter(nicole, veg_r), true, 0). st_hpd(order(nicole, lentil_soup, waitress), true, 1). st_hpd(put_down(waitress, miso_soup, t), true, 2).
```

---

## Story #49 — Partial Match (Similarity: 0.3636)

**Story:** The waiter brought the bill to Mark's table. Mark reviewed it and noticed he had been charged for a dessert he didn't order. He called the waiter over to correct the bill.

### Predicted
```clingo
restaurant(r). customer("Mark"). person("Mark"). food("dessert"). waiter("the waiter"). st_obs(in("Mark", r), true, 0). st_hpd(read_bill("Mark"), true, 1). st_hpd(complain("Mark", "the waiter"), true, 2). st_hpd(cancel_bill("the waiter"), true, 3).
```

### Ground Truth
```clingo
restaurant(r). customer("Mark"). food("dessert"). waiter("the waiter"). st_hpd(put_down("the waiter", b, t), true, 0). st_hpd(pick_up("Mark", b, t), true, 1). st_hpd(request("Mark", "correction", "the waiter"), true, 1).
```

---

## Story #6 — Partial Match (Similarity: 0.3750)

**Story:** Molly is seated at her table when the waiter asks for her order. She orders a baked potato. The waiter brings out French fries.

### Predicted
```clingo
restaurant("the restaurant"). customer("Molly"). person("Molly"). waiter("the waiter"). food("a baked potato"). food("French fries"). st_obs(sitting("Molly"), true, 0). st_obs(at_l("Molly", t), true, 0). st_hpd(greet("the waiter", "Molly"), true, 1). st_hpd(order("Molly", "a baked potato", "the waiter"), true, 2). st_hpd(prepare(c, "French fries", "the waiter"), true, 3). st_obs(food_prepared(c, "French fries", "the waiter"), true, 3). st_hpd(move("the waiter", l1, t), true, 4). st_hpd(put_down("the waiter", "French fries", t), true, 4). st_obs(served("Molly"), true, 4).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer("Molly"). food("baked potato"). food("French fries"). waiter("the waiter"). story_step(0..2). st_obs(sitting("Molly"), true, 0). st_hpd(order("Molly", "baked potato", "the waiter"), true, 1). st_hpd(put_down("the waiter", "French fries", t), true, 2).
```

---

## Story #60 — Partial Match (Similarity: 0.3750)

**Story:** Robert ordered a medium-rare steak but received a well-done one. He called the waiter and complained about the mistake. The waiter apologized and took the steak back to the kitchen.

### Predicted
```clingo
person("Robert"). waiter("the waiter"). food("medium-rare steak"). food("well-done steak"). st_hpd(order("Robert", "medium-rare steak", "the waiter"), true, 0). st_obs(served("Robert"), true, 1). st_obs(holding("the waiter", "well-done steak"), true, 1). st_hpd(complain("Robert", "the waiter"), true, 2). st_hpd(request("Robert", "the waiter", "the waiter"), true, 2). st_hpd(informed("Robert", "mistake", "the waiter"), true, 2). st_hpd(move("the waiter", t, "kitchen"), true, 3). st_hpd(put_down("the waiter", "well-done steak", "kitchen"), true, 3).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer("Robert"). food("medium-rare steak"). food("well-done steak"). waiter("the waiter"). story_step(0..3). st_hpd(order("Robert", "medium-rare steak", "the waiter"), true, 0). st_hpd(put_down("the waiter", "well-done steak", t), true, 1). st_hpd(complain("Robert", "the waiter"), true, 2). st_next(1, 2). st_hpd(pick_up("the waiter", "well-done steak", t), true, 3).
```

---

## Story #70 — Partial Match (Similarity: 0.3810)

**Story:** The Jackson family went to a pizzeria on Friday night. The waiter led them to a booth. They ordered a large pepperoni pizza and a pitcher of soda. The waiter brought their order to the table. They all loved the pizza.

### Predicted
```clingo
restaurant("pizzeria"). customer("Jackson family"). person("Jackson family"). waiter("the waiter"). food("large pepperoni pizza"). beverage("pitcher of soda"). member("Jackson family", "Jackson family"). st_hpd(enter("Jackson family", "pizzeria"), true, 0). st_hpd(lead_to("the waiter", "Jackson family", t), true, 1). st_hpd(order("Jackson family", "large pepperoni pizza", "the waiter"), true, 2). st_hpd(order("Jackson family", "pitcher of soda", "the waiter"), true, 3). st_hpd(move("the waiter", w, t), true, 4). st_obs(holding("the waiter", "large pepperoni pizza"), true, 4). st_obs(holding("the waiter", "pitcher of soda"), true, 4). st_hpd(put_down("the waiter", "large pepperoni pizza", t), true, 5). st_hpd(put_down("the waiter", "pitcher of soda", t), true, 5). st_hpd(eat("Jackson family", "large pepperoni pizza"), true, 6). st_hpd(drink("Jackson family", "pitcher of soda"), true, 6).
```

### Ground Truth
```clingo
restaurant("pizzeria"). customer("The Jackson family"). food("large pepperoni pizza"). beverage("pitcher of soda"). waiter("the waiter"). st_hpd(enter("The Jackson family", "pizzeria"), true, 0). st_hpd(lead_to("the waiter", "The Jackson family", t), true, 1). st_hpd(order("The Jackson family", "large pepperoni pizza", "the waiter"), true, 2). st_hpd(order("The Jackson family", "pitcher of soda", "the waiter"), true, 2). st_hpd(put_down("the waiter", "large pepperoni pizza", t), true, 3). st_hpd(put_down("the waiter", "pitcher of soda", t), true, 3). st_hpd(eat("The Jackson family", "large pepperoni pizza"), true, 4).
```

---

## Story #44 — Partial Match (Similarity: 0.3846)

**Story:** At an Italian restaurant, Chloe ordered lasagna. The waiter brought her spaghetti instead. Chloe informed the waiter of the mistake.

### Predicted
```clingo
restaurant("Italian restaurant"). customer("Chloe"). person("Chloe"). food("lasagna"). food("spaghetti"). waiter("the waiter"). st_obs(in("Chloe", "Italian restaurant"), true, 0). st_hpd(order("Chloe", "lasagna", "the waiter"), true, 1). st_hpd(prepare("cook", "spaghetti", "the waiter"), true, 2). st_hpd(complain("Chloe", "the waiter"), true, 3).
```

### Ground Truth
```clingo
restaurant("Italian restaurant"). customer("Chloe"). food("lasagna"). food("spaghetti"). waiter("the waiter"). story_step(0..2). st_hpd(order("Chloe", "lasagna", "the waiter"), true, 0). st_hpd(put_down("the waiter", "spaghetti", t), true, 1). st_hpd(complain("Chloe", "the waiter"), true, 2). st_next(1, 2).
```

---

## Story #61 — Partial Match (Similarity: 0.3846)

**Story:** The book club members met at the quiet cafe. They ordered various teas and pastries. Everyone enjoyed their selections while discussing the latest novel.

### Predicted
```clingo
person("the book club members"). customer("the book club members"). restaurant("the quiet cafe"). beverage("various teas"). food("pastries"). st_hpd(enter("the book club members", "the quiet cafe"), true, 0). st_hpd(order("the book club members", "various teas", w), true, 1). st_hpd(order("the book club members", "pastries", w), true, 1). st_hpd(eat("the book club members", "pastries"), true, 2). st_hpd(drink("the book club members", "various teas"), true, 2).
```

### Ground Truth
```clingo
restaurant("quiet cafe"). customer("book club members"). food("pastries"). beverage("teas"). story_step(0..2). st_hpd(enter("book club members", "quiet cafe"), true, 0). st_hpd(order("book club members", "pastries", "the waiter"), true, 1). st_hpd(order("book club members", "teas", "the waiter"), true, 1). st_hpd(eat("book club members", "pastries"), true, 2). st_hpd(drink("book club members", "teas"), true, 2).
```

---

## Story #11 — Partial Match (Similarity: 0.4000)

**Story:** Jake is seated at his table in the restaurant. He orders a medium-rare steak. The waiter brings out his order but it is too rare.

### Predicted
```clingo
restaurant("the restaurant"). customer("Jake"). person("Jake"). food("medium-rare steak"). waiter("the waiter"). st_obs(sitting("Jake"), true, 0). st_obs(at_l("Jake", t), true, 0). st_obs(in("Jake", "the restaurant"), true, 0). st_hpd(order("Jake", "medium-rare steak", "the waiter"), true, 1). st_hpd(prepare("the cook", "medium-rare steak", "the waiter"), true, 2). st_hpd(move("the waiter", "the kitchen", t), true, 3). st_obs(holding("the waiter", "medium-rare steak"), true, 3). st_hpd(put_down("the waiter", "medium-rare steak", t), true, 4). st_obs(served("Jake"), true, 4).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer("Jake"). food("medium-rare steak"). food("too rare steak"). waiter("the waiter"). story_step(0..2). st_obs(sitting("Jake"), true, 0). st_hpd(order("Jake", "medium-rare steak", "the waiter"), true, 1). st_hpd(put_down("the waiter", "too rare steak", t), true, 2).
```

---

## Story #87 — Partial Match (Similarity: 0.4000)

**Story:** [REDACTED — original ROCStories text; storyid=7dc0c96f-dd24-4561-9a4f-bd1b6b3ca520]

### Predicted
```clingo
restaurant("the restaurant"). customer("I"). person("I"). st_hpd(enter("I", "the restaurant"), true, 0). st_obs(in("I", "the restaurant"), true, 0). st_hpd(order("I", f, w), true, 1). st_hpd(complain("I", w), true, 2).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer("I"). food("wrong order"). st_hpd(enter("I", "the restaurant"), true, 0). st_hpd(order("I", f, w), true, 1). st_hpd(put_down(w, "wrong order", t), true, 2). st_hpd(request("I", pick_up(w, "burnt pizza", t), w), true, 3). st_next(2,3).
```

---

## Story #62 — Partial Match (Similarity: 0.4286)

**Story:** The waiter at the steakhouse brought a rare steak for Wendy, but she had ordered it well-done. She sent it back to the kitchen to be cooked more.

### Predicted
```clingo
person("Wendy"). customer("Wendy"). waiter("the waiter"). restaurant("the steakhouse"). food("rare steak"). food("well-done steak"). st_hpd(order("Wendy", "well-done steak", "the waiter"), true, 0). st_obs(served("Wendy"), true, 1). st_obs(holding("the waiter", "rare steak"), true, 1). st_hpd(request("Wendy", "the waiter", "the waiter"), true, 2). st_hpd(move("the waiter", t, "kitchen"), true, 3). st_hpd(put_down("the waiter", "rare steak", "kitchen"), true, 3).
```

### Ground Truth
```clingo
restaurant("the steakhouse"). customer("Wendy"). food("rare steak"). food("well-done steak"). waiter("the waiter"). story_step(0..2). st_hpd(order("Wendy", "well-done steak", "the waiter"), true, 0). st_hpd(put_down("the waiter", "rare steak", t), true, 1). st_hpd(request("Wendy", pick_up("the waiter", "rare steak", t), "the waiter"), true, 2). st_next(1, 2).
```

---

## Story #45 — Partial Match (Similarity: 0.4444)

**Story:** The restaurant was very busy. A group of friends was seated, but no waiter came to take their order. After waiting for twenty minutes, they decided to leave and go somewhere else.

### Predicted
```clingo
restaurant(r). customer("group of friends"). person("group of friends"). waiter(w). st_obs(in("group of friends", r), true, 0). st_obs(sitting("group of friends"), true, 0). st_hpd(order("group of friends"), false). st_hpd(leave("group of friends"), true, 1).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer("group of friends"). waiter(w). story_step(0..2). st_obs(sitting("group of friends"), true, 0). st_hpd(served("group of friends"), false). st_hpd(leave("group of friends"), true, 1).
```

---

## Story #54 — Partial Match (Similarity: 0.4444)

**Story:** Sarah visited the cafe for lunch. She sat at a table by the window and ordered a chicken sandwich and coffee. The waitress brought her order. Sarah ate quickly as she was in a hurry.

### Predicted
```clingo
person("Sarah"). customer("Sarah"). waiter("the waitress"). food("chicken sandwich"). beverage("coffee"). restaurant("cafe"). st_hpd(enter("Sarah", "cafe"), true, 0). st_hpd(sit("Sarah"), true, 1). st_hpd(order("Sarah", "chicken sandwich", "the waitress"), true, 2). st_hpd(order("Sarah", "coffee", "the waitress"), true, 2). st_hpd(eat("Sarah", "chicken sandwich"), true, 3). st_hpd(drink("Sarah", "coffee"), true, 3). st_obs(in("Sarah", "cafe"), true, 0). st_obs(at_l("Sarah", t), true, 1). st_obs(sitting("Sarah"), true, 1). st_obs(served("Sarah"), true, 3).
```

### Ground Truth
```clingo
restaurant("the cafe"). customer("Sarah"). food("chicken sandwich"). beverage("coffee"). waiter("the waitress"). story_step(0..4). st_hpd(enter("Sarah", "the cafe"), true, 0). st_hpd(sit("Sarah"), true, 1). st_hpd(order("Sarah", "chicken sandwich", "the waitress"), true, 2). st_hpd(put_down("the waitress", "chicken sandwich", t), true, 3). st_hpd(eat("Sarah", "chicken sandwich"), true, 4). st_hpd(drink("Sarah", "coffee"), true, 4).
```

---

## Story #48 — Partial Match (Similarity: 0.4545)

**Story:** Olivia sat down at a table. The waiter greeted her and took her drink order: a glass of water. The waiter brought the water.

### Predicted
```clingo
restaurant(r). customer("Olivia"). person("Olivia"). beverage("water"). waiter("the waiter"). st_hpd(sit("Olivia"), true, 0). st_hpd(greet("the waiter", "Olivia"), true, 1). st_hpd(order("Olivia", "water", "the waiter"), true, 2). st_hpd(drink("Olivia", "water"), true, 3).
```

### Ground Truth
```clingo
restaurant(r). customer("Olivia"). beverage("glass of water"). waiter("the waiter"). story_step(0..3). st_hpd(sit("Olivia"), true, 0). st_hpd(greet("the waiter", "Olivia"), true, 1). st_hpd(order("Olivia", "glass of water", "the waiter"), true, 2). st_hpd(put_down("the waiter", "glass of water", t), true, 3).
```

---

## Story #81 — Partial Match (Similarity: 0.4615)

**Story:** [REDACTED — original ROCStories text; storyid=1d235832-c133-4950-ba20-512adb2e3edb]

### Predicted
```clingo
restaurant("new Italian restaurant"). customer("Kathy"). customer("her friend"). person("Kathy"). person("her friend"). member("Kathy", "they"). member("her friend", "they"). st_hpd(enter("they", "new Italian restaurant"), true, 0). st_obs(in("they", "new Italian restaurant"), true, 0). st_hpd(order("they", f, w), true, 1). st_hpd(eat("they", f), true, 2). st_hpd(leave("they"), true, 3).
```

### Ground Truth
```clingo
restaurant("new Italian restaurant"). customer(they). person("Kathy"). person("her friend"). member("Kathy", they). member("her friend", they). food("dinner"). st_hpd(enter(they, "new Italian restaurant"), true, 0). st_hpd(eat(they, "dinner"), true, 1).
```

---

## Story #26 — Partial Match (Similarity: 0.5000)

**Story:** Nicole went to a vegetarian restaurant. She ordered lentil soup. The waitress set the soup in the middle of the table. Nicole enjoyed the soup. She left the restaurant.

### Predicted
```clingo
restaurant("vegetarian restaurant"). customer("Nicole"). person("Nicole"). waiter("waitress"). food("lentil soup"). st_hpd(enter("Nicole", "vegetarian restaurant"), true, 0). st_hpd(order("Nicole", "lentil soup", "waitress"), true, 1). st_hpd(bring("waitress", "lentil soup", "table"), true, 2). st_hpd(eat("Nicole", "lentil soup"), true, 3). st_hpd(leave("Nicole"), true, 4).
```

### Ground Truth
```clingo
restaurant(veg_r). customer(nicole). food(lentil_soup). waiter(waitress). story_step(0..4). st_hpd(enter(nicole, veg_r), true, 0). st_hpd(order(nicole, lentil_soup, waitress), true, 1). st_hpd(put_down(waitress, lentil_soup, t), true, 2). st_hpd(eat(nicole, lentil_soup), true, 3). st_hpd(leave(nicole), true, 4).
```

---

## Story #50 — Partial Match (Similarity: 0.5000)

**Story:** Fiona ordered the soup of the day. The waiter returned a minute later to inform her that they had just run out of the soup. Fiona then ordered a sandwich instead.

### Predicted
```clingo
person("Fiona"). customer("Fiona"). waiter("the waiter"). food("soup of the day"). food("sandwich"). restaurant("the restaurant"). st_hpd(order("Fiona", "soup of the day", "the waiter"), true, 0). st_hpd(inform("the waiter", "run out of soup", "Fiona"), true, 1). st_hpd(order("Fiona", "sandwich", "the waiter"), true, 2). st_hpd(make_unavailable("soup of the day", "the restaurant"), true, 1). st_obs(available("soup of the day", "the restaurant"), false, 1).
```

### Ground Truth
```clingo
restaurant(r). customer("Fiona"). food("soup of the day"). food("sandwich"). waiter("the waiter"). story_step(0..2). st_hpd(order("Fiona", "soup of the day", "the waiter"), true, 0). st_obs(available("soup of the day", r), false, 1). st_hpd(order("Fiona", "sandwich", "the waiter"), true, 2).
```

---

## Story #89 — Partial Match (Similarity: 0.5000)

**Story:** [REDACTED — original ROCStories text; storyid=c93ca5db-716f-4572-868e-bd22aa4a9018]

### Predicted
```clingo
restaurant("Genki Ya"). customer("my son"). customer("me"). person("my son"). person("me"). person("my wife"). food("sashimi"). member("my son", "we"). member("me", "we"). st_hpd(enter("we", "Genki Ya"), true, 0). st_obs(in("we", "Genki Ya"), true, 0). st_hpd(order("we", f, w), true, 1). st_hpd(eat("we", f), true, 2). st_hpd(leave("we"), true, 3).
```

### Ground Truth
```clingo
restaurant("Genki Ya"). customer(we). person("my son"). person("me"). member("my son", we). member("me", we). food("sashimi"). st_hpd(enter(we, "Genki Ya"), true, 0). st_hpd(eat(we, "sashimi"), true, 1).
```

---

## Story #43 — Partial Match (Similarity: 0.5385)

**Story:** Megan entered the restaurant and sat at the bar. She ordered a glass of wine from the bartender. She finished her drink, paid the bartender, and left.

### Predicted
```clingo
restaurant("the restaurant"). customer("Megan"). person("Megan"). beverage("wine"). waiter("the bartender"). st_hpd(enter("Megan", "the restaurant"), true, 0). st_hpd(sit("Megan"), true, 1). st_hpd(order("Megan", "wine", "the bartender"), true, 2). st_hpd(drink("Megan", "wine"), true, 3). st_hpd(pay("Megan", b), true, 4). st_hpd(leave("Megan"), true, 5).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer("Megan"). beverage("glass of wine"). waiter("the bartender"). st_hpd(enter("Megan", "the restaurant"), true, 0). st_hpd(sit("Megan"), true, 1). st_hpd(order("Megan", "glass of wine", "the bartender"), true, 2). st_hpd(drink("Megan", "glass of wine"), true, 3). st_hpd(pay("Megan", b), true, 4). st_hpd(leave("Megan"), true, 5).
```

---

## Story #4 — Partial Match (Similarity: 0.5556)

**Story:** Bob is seated at a table in the restaurant. The waiter asks for his order, and he orders a hamburger.

### Predicted
```clingo
restaurant("the restaurant"). customer("Bob"). person("Bob"). waiter("the waiter"). food("a hamburger"). st_obs(sitting("Bob"), true, 0). st_obs(at_l("Bob", t), true, 0). st_hpd(greet("the waiter", "Bob"), true, 1). st_hpd(order("Bob", "a hamburger", "the waiter"), true, 2).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer("Bob"). food("hamburger"). waiter("the waiter"). story_step(0..1). st_obs(sitting("Bob"), true, 0). st_hpd(order("Bob", "hamburger", "the waiter"), true, 1).
```

---

## Story #68 — Partial Match (Similarity: 0.7143)

**Story:** Frank sat down at his usual table in the local diner. The waitress brought him a black coffee. Frank looked at the menu and then ordered pancakes. He ate them, left cash on the table for the bill, and left.

### Predicted
```clingo
person("Frank"). customer("Frank"). waiter("the waitress"). restaurant("the local diner"). beverage("black coffee"). food("pancakes"). st_hpd(sit("Frank"), true, 0). st_obs(served("Frank"), true, 1). st_hpd(read_menu("Frank"), true, 2). st_hpd(order("Frank", "pancakes", "the waitress"), true, 3). st_hpd(eat("Frank", "pancakes"), true, 4). st_hpd(pay("Frank", b), true, 5). st_hpd(leave("Frank"), true, 6).
```

### Ground Truth
```clingo
restaurant("local diner"). customer("Frank"). beverage("black coffee"). food("pancakes"). waiter("the waitress"). story_step(0..6). st_obs(sitting("Frank"), true, 0). st_hpd(put_down("the waitress", "black coffee", t), true, 1). st_hpd(read_menu("Frank"), true, 2). st_hpd(order("Frank", "pancakes", "the waitress"), true, 3). st_hpd(eat("Frank", "pancakes"), true, 4). st_hpd(pay("Frank", b), true, 5). st_hpd(leave("Frank"), true, 6).
```

---

## Story #59 — Partial Match (Similarity: 0.8182)

**Story:** Lucy visited the health food restaurant. She ordered a kale salad and detox juice. The ingredients were fresh and organic. She felt energized after her meal.

### Predicted
```clingo
person("Lucy"). customer("Lucy"). food("kale salad"). beverage("detox juice"). restaurant("health food restaurant"). st_hpd(enter("Lucy", "health food restaurant"), true, 0). st_hpd(order("Lucy", "kale salad", "the waiter"), true, 1). st_hpd(order("Lucy", "detox juice", "the waiter"), true, 1). st_hpd(eat("Lucy", "kale salad"), true, 2). st_hpd(drink("Lucy", "detox juice"), true, 2). st_obs(in("Lucy", "health food restaurant"), true, 0). st_obs(served("Lucy"), true, 2).
```

### Ground Truth
```clingo
restaurant("health food restaurant"). customer("Lucy"). food("kale salad"). beverage("detox juice"). story_step(0..2). st_hpd(enter("Lucy", "health food restaurant"), true, 0). st_hpd(order("Lucy", "kale salad", "the waiter"), true, 1). st_hpd(order("Lucy", "detox juice", "the waiter"), true, 1). st_hpd(eat("Lucy", "kale salad"), true, 2). st_hpd(drink("Lucy", "detox juice"), true, 2).
```

---
