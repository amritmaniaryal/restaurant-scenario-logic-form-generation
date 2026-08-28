# 10_gemini_v3.0_evaluated

## Summary

- Total common: 100
- Exact matches: 18
- Partial matches: 82
- Accuracy: 0.18

---

## Story #1 — Exact Match (Similarity: 1.0000)

**Story:** Abdul is sitting in a vegetarian restaurant. The waiter takes his order, and he orders hummus. The waiter brings the hummus to the table.

### Predicted
```clingo
restaurant("vegetarian restaurant"). customer("Abdul"). food("hummus"). waiter("the waiter"). st_obs(sitting("Abdul"), true, 0). st_hpd(order("Abdul", "hummus", "the waiter"), true, 1). st_hpd(put_down("the waiter", "hummus", t), true, 2).
```

### Ground Truth
```clingo
restaurant("vegetarian restaurant"). customer("Abdul"). food("hummus"). waiter("the waiter"). story_step(0..2). st_obs(sitting("Abdul"), true, 0). st_hpd(order("Abdul", "hummus", "the waiter"), true, 1). st_hpd(put_down("the waiter", "hummus", t), true, 2).
```

---

## Story #2 — Exact Match (Similarity: 1.0000)

**Story:** John enters the restaurant. The waiter escorts him to a table. John orders steak. The waiter brings the steak to the table. John asks for the bill, and the waiter brings it to the table. John pays the bill and leaves the restaurant.

### Predicted
```clingo
restaurant("the restaurant"). customer("John"). food("steak"). waiter("the waiter"). st_hpd(enter("John", "the restaurant"), true, 0). st_hpd(lead_to("the waiter", "John", t), true, 1). st_hpd(order("John", "steak", "the waiter"), true, 2). st_hpd(put_down("the waiter", "steak", t), true, 3). st_hpd(request("John", b, "the waiter"), true, 4). st_hpd(put_down("the waiter", b, t), true, 5). st_hpd(pay("John", b), true, 6). st_hpd(leave("John"), true, 7).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer("John"). food("steak"). waiter("the waiter"). story_step(0..6). st_hpd(enter("John", "the restaurant"), true, 0). st_hpd(lead_to("the waiter", "John", t), true, 1). st_hpd(order("John", "steak", "the waiter"), true, 2). st_hpd(put_down("the waiter", "steak", t), true, 3). st_hpd(request("John", b, "the waiter"), true, 4). st_hpd(put_down("the waiter", b, t), true, 5). st_hpd(pay("John", b), true, 6). st_hpd(leave("John"), true, 7).
```

---

## Story #3 — Exact Match (Similarity: 1.0000)

**Story:** Jill enters the restaurant and is escorted to a table. She orders chicken. The waiter brings the chicken to her table. After eating, Jill asks for the bill.

### Predicted
```clingo
restaurant("the restaurant"). customer("Jill"). food("chicken"). waiter("the waiter"). st_hpd(enter("Jill", "the restaurant"), true, 0). st_hpd(lead_to("the waiter", "Jill", t), true, 1). st_hpd(order("Jill", "chicken", "the waiter"), true, 2). st_hpd(put_down("the waiter", "chicken", t), true, 3). st_hpd(eat("Jill", "chicken"), true, 4). st_hpd(request("Jill", b, "the waiter"), true, 5).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer("Jill"). food("chicken"). waiter("the waiter"). story_step(0..5). st_hpd(enter("Jill", "the restaurant"), true, 0). st_hpd(lead_to("the waiter", "Jill", t), true, 1). st_hpd(order("Jill", "chicken", "the waiter"), true, 2). st_hpd(put_down("the waiter", "chicken", t), true, 3). st_hpd(eat("Jill", "chicken"), true, 4). st_hpd(request("Jill", b, "the waiter"), true, 5).
```

---

## Story #4 — Exact Match (Similarity: 1.0000)

**Story:** Bob is seated at a table in the restaurant. The waiter asks for his order, and he orders a hamburger.

### Predicted
```clingo
restaurant("the restaurant"). customer("Bob"). food("hamburger"). waiter("the waiter"). st_obs(sitting("Bob"), true, 0). st_hpd(order("Bob", "hamburger", "the waiter"), true, 1).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer("Bob"). food("hamburger"). waiter("the waiter"). story_step(0..1). st_obs(sitting("Bob"), true, 0). st_hpd(order("Bob", "hamburger", "the waiter"), true, 1).
```

---

## Story #5 — Exact Match (Similarity: 1.0000)

**Story:** The waiter shows Jane to her table. Jane is seated at a table in the restaurant. The waiter asks for her order, and she orders fish. After eating, the waiter brings the bill to the table.

### Predicted
```clingo
restaurant("the restaurant"). customer("Jane"). food("fish"). waiter("the waiter"). story_step(0..4). st_hpd(lead_to("the waiter", "Jane", t), true, 0). st_obs(sitting("Jane"), true, 1). st_hpd(order("Jane", "fish", "the waiter"), true, 2). st_hpd(eat("Jane", "fish"), true, 3). st_hpd(put_down("the waiter", b, t), true, 4).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer("Jane"). food("fish"). waiter("the waiter"). story_step(0..4). st_hpd(lead_to("the waiter", "Jane", t), true, 0). st_obs(sitting("Jane"), true, 1). st_hpd(order("Jane", "fish", "the waiter"), true, 2). st_hpd(eat("Jane", "fish"), true, 3). st_hpd(put_down("the waiter", b, t), true, 4).
```

---

## Story #6 — Exact Match (Similarity: 1.0000)

**Story:** Molly is seated at her table when the waiter asks for her order. She orders a baked potato. The waiter brings out French fries.

### Predicted
```clingo
restaurant("the restaurant"). customer("Molly"). food("baked potato"). food("French fries"). waiter("the waiter"). story_step(0..2). st_obs(sitting("Molly"), true, 0). st_hpd(order("Molly", "baked potato", "the waiter"), true, 1). st_hpd(put_down("the waiter", "French fries", t), true, 2).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer("Molly"). food("baked potato"). food("French fries"). waiter("the waiter"). story_step(0..2). st_obs(sitting("Molly"), true, 0). st_hpd(order("Molly", "baked potato", "the waiter"), true, 1). st_hpd(put_down("the waiter", "French fries", t), true, 2).
```

---

## Story #7 — Exact Match (Similarity: 1.0000)

**Story:** Larry is seated at his table in the restaurant. The waiter brings him a menu so he can decide what to order. After reviewing the menu, Larry decides he doesn't want anything at this restaurant.

### Predicted
```clingo
restaurant("the restaurant"). customer("Larry"). waiter("the waiter"). story_step(0..3). st_obs(sitting("Larry"), true, 0). st_hpd(put_down("the waiter", m, t), true, 1). st_obs(menu_read("Larry"), true, 2). st_hpd(order("Larry"), false, 3).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer("Larry"). waiter("the waiter"). story_step(0..3). st_obs(sitting("Larry"), true, 0). st_hpd(put_down("the waiter", m, t), true, 1). st_obs(menu_read("Larry"), true, 2). st_hpd(order("Larry"), false, 3).
```

---

## Story #14 — Exact Match (Similarity: 1.0000)

**Story:** Samantha was in a five-star restaurant. Samantha started perusing the menu. She ordered the barbecued veal chop with Asian slaw and Thai fried rice.

### Predicted
```clingo
restaurant("five-star restaurant"). customer("Samantha"). food("barbecued veal chop with Asian slaw and Thai fried rice"). st_obs(in("Samantha", "five-star restaurant"), true, 0). st_hpd(read_menu("Samantha"), true, 1). st_hpd(order("Samantha", "barbecued veal chop with Asian slaw and Thai fried rice", w), true, 2).
```

### Ground Truth
```clingo
restaurant("a five-star restaurant"). customer("Samantha"). food("barbecued veal chop with Asian slaw and Thai fried rice"). story_step(0..2). st_obs(in("Samantha", "a five-star restaurant"), true, 0). st_hpd(read_menu("Samantha"), true, 1). st_hpd(order("Samantha", "barbecued veal chop with Asian slaw and Thai fried rice", w), true, 2).
```

---

## Story #15 — Exact Match (Similarity: 1.0000)

**Story:** The villager entered a fine restaurant and was seated at one of the tables. He looked at the menu. He ordered one of the items on the list. The waiter brought him a large plate of lettuce salad with several black olives on top.

### Predicted
```clingo
restaurant("a fine restaurant"). customer("the villager"). food("one of the items on the list"). food("lettuce salad with several black olives on top"). story_step(0..4). st_hpd(enter("the villager", "a fine restaurant"), true, 0). st_obs(sitting("the villager"), true, 1). st_hpd(pick_up("the villager", m, t), true, 2). st_hpd(order("the villager", "one of the items on the list", w), true, 3). st_hpd(put_down(w, "lettuce salad with several black olives on top", t), true, 4).
```

### Ground Truth
```clingo
restaurant("a fine restaurant"). customer("the villager"). food("one of the items on the list"). food("lettuce salad with several black olives on top"). story_step(0..4). st_hpd(enter("the villager", "a fine restaurant"), true, 0). st_obs(sitting("the villager"), true, 1). st_hpd(pick_up("the villager", m, t), true, 2). st_hpd(order("the villager", "one of the items on the list", w), true, 3). st_hpd(put_down(w, "lettuce salad with several black olives on top", t), true, 4).
```

---

## Story #43 — Exact Match (Similarity: 1.0000)

**Story:** Megan entered the restaurant and sat at the bar. She ordered a glass of wine from the bartender. She finished her drink, paid the bartender, and left.

### Predicted
```clingo
restaurant("the restaurant"). customer("Megan"). beverage("glass of wine"). waiter("the bartender"). st_hpd(enter("Megan", "the restaurant"), true, 0). st_hpd(sit("Megan"), true, 1). st_hpd(order("Megan", "glass of wine", "the bartender"), true, 2). st_hpd(drink("Megan", "glass of wine"), true, 3). st_hpd(pay("Megan", b), true, 4). st_hpd(leave("Megan"), true, 5).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer("Megan"). beverage("glass of wine"). waiter("the bartender"). st_hpd(enter("Megan", "the restaurant"), true, 0). st_hpd(sit("Megan"), true, 1). st_hpd(order("Megan", "glass of wine", "the bartender"), true, 2). st_hpd(drink("Megan", "glass of wine"), true, 3). st_hpd(pay("Megan", b), true, 4). st_hpd(leave("Megan"), true, 5).
```

---

## Story #48 — Exact Match (Similarity: 1.0000)

**Story:** Olivia sat down at a table. The waiter greeted her and took her drink order: a glass of water. The waiter brought the water.

### Predicted
```clingo
restaurant(r). customer("Olivia"). beverage("glass of water"). waiter("The waiter"). st_hpd(sit("Olivia"), true, 0). st_hpd(greet("The waiter", "Olivia"), true, 1). st_hpd(order("Olivia", "glass of water", "The waiter"), true, 2). st_hpd(put_down("The waiter", "glass of water", t), true, 3).
```

### Ground Truth
```clingo
restaurant(r). customer("Olivia"). beverage("glass of water"). waiter("the waiter"). story_step(0..3). st_hpd(sit("Olivia"), true, 0). st_hpd(greet("the waiter", "Olivia"), true, 1). st_hpd(order("Olivia", "glass of water", "the waiter"), true, 2). st_hpd(put_down("the waiter", "glass of water", t), true, 3).
```

---

## Story #50 — Exact Match (Similarity: 1.0000)

**Story:** Fiona ordered the soup of the day. The waiter returned a minute later to inform her that they had just run out of the soup. Fiona then ordered a sandwich instead.

### Predicted
```clingo
restaurant(r). customer("Fiona"). food("soup of the day"). food("sandwich"). waiter("the waiter"). story_step(0..2). st_hpd(order("Fiona", "soup of the day", "the waiter"), true, 0). st_obs(available("soup of the day", r), false, 1). st_hpd(order("Fiona", "sandwich", "the waiter"), true, 2).
```

### Ground Truth
```clingo
restaurant(r). customer("Fiona"). food("soup of the day"). food("sandwich"). waiter("the waiter"). story_step(0..2). st_hpd(order("Fiona", "soup of the day", "the waiter"), true, 0). st_obs(available("soup of the day", r), false, 1). st_hpd(order("Fiona", "sandwich", "the waiter"), true, 2).
```

---

## Story #57 — Exact Match (Similarity: 1.0000)

**Story:** Carlos arrived at the Mexican restaurant and was greeted warmly. He ordered tacos and a margarita. The food arrived quickly and was perfectly prepared. Carlos enjoyed his meal thoroughly.

### Predicted
```clingo
restaurant("Mexican restaurant"). customer("Carlos"). food("tacos"). beverage("margarita"). waiter(w). st_hpd(enter("Carlos", "Mexican restaurant"), true, 0). st_hpd(greet(w, "Carlos"), true, 1). st_hpd(order("Carlos", "tacos", w), true, 2). st_hpd(order("Carlos", "margarita", w), true, 2). st_hpd(put_down(w, "tacos", t), true, 3). st_hpd(put_down(w, "margarita", t), true, 3). st_hpd(eat("Carlos", "tacos"), true, 4). st_hpd(drink("Carlos", "margarita"), true, 4).
```

### Ground Truth
```clingo
restaurant("Mexican restaurant"). customer("Carlos"). waiter(w). food("tacos"). beverage("margarita"). story_step(0..4). st_hpd(enter("Carlos", "Mexican restaurant"), true, 0). st_hpd(greet(w, "Carlos"), true, 1). st_hpd(order("Carlos", "tacos", w), true, 2). st_hpd(order("Carlos", "margarita", w), true, 2). st_hpd(put_down(w, "tacos", t), true, 3). st_hpd(put_down(w, "margarita", t), true, 3). st_hpd(eat("Carlos", "tacos"), true, 4). st_hpd(drink("Carlos", "margarita"), true, 4).
```

---

## Story #59 — Exact Match (Similarity: 1.0000)

**Story:** Lucy visited the health food restaurant. She ordered a kale salad and detox juice. The ingredients were fresh and organic. She felt energized after her meal.

### Predicted
```clingo
restaurant("health food restaurant"). customer("Lucy"). food("kale salad"). beverage("detox juice"). story_step(0..2). st_hpd(enter("Lucy", "health food restaurant"), true, 0). st_hpd(order("Lucy", "kale salad", "the waiter"), true, 1). st_hpd(order("Lucy", "detox juice", "the waiter"), true, 1). st_hpd(eat("Lucy", "kale salad"), true, 2). st_hpd(drink("Lucy", "detox juice"), true, 2).
```

### Ground Truth
```clingo
restaurant("health food restaurant"). customer("Lucy"). food("kale salad"). beverage("detox juice"). story_step(0..2). st_hpd(enter("Lucy", "health food restaurant"), true, 0). st_hpd(order("Lucy", "kale salad", "the waiter"), true, 1). st_hpd(order("Lucy", "detox juice", "the waiter"), true, 1). st_hpd(eat("Lucy", "kale salad"), true, 2). st_hpd(drink("Lucy", "detox juice"), true, 2).
```

---

## Story #63 — Exact Match (Similarity: 1.0000)

**Story:** At a cafe, Ivan ordered an espresso. The waiter brought it to his table. Ivan drank the espresso, left cash on the table for the bill, and then departed.

### Predicted
```clingo
restaurant("cafe"). customer("Ivan"). beverage("espresso"). waiter("The waiter"). st_hpd(order("Ivan", "espresso", "The waiter"), true, 0). st_hpd(put_down("The waiter", "espresso", t), true, 1). st_hpd(drink("Ivan", "espresso"), true, 2). st_hpd(pay("Ivan", b), true, 3). st_hpd(leave("Ivan"), true, 4).
```

### Ground Truth
```clingo
restaurant("cafe"). customer("Ivan"). beverage("espresso"). waiter("the waiter"). story_step(0..4). st_hpd(order("Ivan", "espresso", "the waiter"), true, 0). st_hpd(put_down("the waiter", "espresso", t), true, 1). st_hpd(drink("Ivan", "espresso"), true, 2). st_hpd(pay("Ivan", b), true, 3). st_hpd(leave("Ivan"), true, 4).
```

---

## Story #66 — Exact Match (Similarity: 1.0000)

**Story:** Charlie entered a restaurant and was led to a table. He ordered a burger. The waiter brought the burger. Charlie ate it, asked for the bill, paid, and left.

### Predicted
```clingo
restaurant("restaurant"). customer("Charlie"). food("burger"). waiter("The waiter"). st_hpd(enter("Charlie", "restaurant"), true, 0). st_hpd(lead_to("The waiter", "Charlie", t), true, 1). st_hpd(order("Charlie", "burger", "The waiter"), true, 2). st_hpd(put_down("The waiter", "burger", t), true, 3). st_hpd(eat("Charlie", "burger"), true, 4). st_hpd(request("Charlie", b, "The waiter"), true, 5). st_hpd(pay("Charlie", b), true, 6). st_hpd(leave("Charlie"), true, 7).
```

### Ground Truth
```clingo
restaurant("a restaurant"). customer("Charlie"). food("burger"). waiter("the waiter"). story_step(0..7). st_hpd(enter("Charlie", "a restaurant"), true, 0). st_hpd(lead_to("the waiter", "Charlie", t), true, 1). st_hpd(order("Charlie", "burger", "the waiter"), true, 2). st_hpd(put_down("the waiter", "burger", t), true, 3). st_hpd(eat("Charlie", "burger"), true, 4). st_hpd(request("Charlie", b, "the waiter"), true, 5). st_hpd(pay("Charlie", b), true, 6). st_hpd(leave("Charlie"), true, 7).
```

---

## Story #74 — Exact Match (Similarity: 1.0000)

**Story:** Lisa and Mark went to the Italian restaurant for their date night. They were seated at a cozy table. Lisa ordered lasagna and Mark ordered chicken parmesan. They shared a bottle of wine with their meal.

### Predicted
```clingo
restaurant("Italian restaurant"). customer("Lisa"). customer("Mark"). customer(they). member("Lisa", they). member("Mark", they). food("lasagna"). food("chicken parmesan"). beverage("wine"). st_hpd(enter(they, "Italian restaurant"), true, 0). st_obs(sitting(they), true, 1). st_hpd(order("Lisa", "lasagna", "the waiter"), true, 2). st_hpd(order("Mark", "chicken parmesan", "the waiter"), true, 2). st_hpd(eat("Lisa", "lasagna"), true, 3). st_hpd(eat("Mark", "chicken parmesan"), true, 3). st_hpd(drink(they, "wine"), true, 3).
```

### Ground Truth
```clingo
restaurant("Italian restaurant"). customer("Lisa"). customer("Mark"). customer(they). member("Lisa", they). member("Mark", they). food("lasagna"). food("chicken parmesan"). beverage("wine"). st_hpd(enter(they, "Italian restaurant"), true, 0). st_obs(sitting(they), true, 1). st_hpd(order("Lisa", "lasagna", "the waiter"), true, 2). st_hpd(order("Mark", "chicken parmesan", "the waiter"), true, 2). st_hpd(eat("Lisa", "lasagna"), true, 3). st_hpd(eat("Mark", "chicken parmesan"), true, 3). st_hpd(drink(they, "wine"), true, 3).
```

---

## Story #92 — Exact Match (Similarity: 1.0000)

**Story:** [REDACTED — original ROCStories text; storyid=c9e533e3-d8cc-4e9c-a7a0-0369d6cdc537]

### Predicted
```clingo
restaurant("new restaurant"). customer("I"). food("large salad"). food("small salad"). waiter(w). st_obs(in("I", "new restaurant"), true, 0). st_hpd(order("I", "large salad", w), true, 1). st_hpd(put_down(w, "small salad", t), true, 2).
```

### Ground Truth
```clingo
restaurant("new restaurant"). customer("I"). food("large salad"). food("small salad"). waiter(w). st_obs(in("I", "new restaurant"), true, 0). st_hpd(order("I", "large salad", w), true, 1). st_hpd(put_down(w, "small salad", t), true, 2).
```

---

## Story #75 — Partial Match (Similarity: 0.0417)

**Story:** [REDACTED — original ROCStories text; storyid=99d073a9-375a-45ad-a070-0fdfbbf73f69]

### Predicted
```clingo
restaurant("Sushi place"). customer("I"). customer("husband"). member("I", they). member("husband", they). food("spicy tuna rolls"). food("eel"). waiter(w). st_hpd(enter(they, "Sushi place"), true, 0). st_hpd(order(they, "spicy tuna rolls", w), true, 1). st_hpd(order(they, "eel", w), true, 1). st_hpd(eat(they, "spicy tuna rolls"), true, 2). st_hpd(eat(they, "eel"), true, 2).
```

### Ground Truth
```clingo
restaurant("new Sushi place"). customer(we). person("I"). person("my husband"). member("I", we). member("my husband", we). food(f). member("spicy tuna rolls", f). member("eel", f). st_hpd(enter(we, "new Sushi place"), true, 0). st_hpd(order(we, f, w), true, 1). st_hpd(eat(we, f), true, 2).
```

---

## Story #12 — Partial Match (Similarity: 0.0714)

**Story:** My husband and I went to a famous restaurant listed in our guidebook. We were seated at a booth and began studying the menu. We ordered escargot, lamb, savory salmon, and a creamy flan dessert.

### Predicted
```clingo
restaurant("famous restaurant"). customer("husband"). customer("I"). member("husband", they). member("I", they). food("escargot"). food("lamb"). food("savory salmon"). food("creamy flan dessert"). st_hpd(enter(they, "famous restaurant"), true, 0). st_obs(sitting(they), true, 1). st_hpd(read_menu(they), true, 2). st_hpd(order(they, "escargot", w), true, 3). st_hpd(order(they, "lamb", w), true, 3). st_hpd(order(they, "savory salmon", w), true, 3). st_hpd(order(they, "creamy flan dessert", w), true, 3).
```

### Ground Truth
```clingo
restaurant("a famous restaurant"). person("my husband"). person("I"). customer("we"). member("my husband", "we"). member("I", "we"). member("escargot", f). member("lamb", f). member("savory salmon", f). member("creamy flan dessert", f) story_step(0..3). st_hpd(enter("we", "a famous restaurant"), true, 0). st_obs(sitting("we"), true, 1). st_hpd(read_menu("we"), true, 2). st_hpd(order("we", f, w), true, 3).
```

---

## Story #24 — Partial Match (Similarity: 0.0714)

**Story:** Jasper invited Frank to a restaurant. Jasper ordered roast beef and coffee. Their conversation was interrupted by the arrival of the coffee and roast beef, which both he and his new friend attacked with vigor. Jasper wanted to invite Frank, but he had forgotten his wallet at home. Frank paid for both.

### Predicted
```clingo
restaurant("restaurant"). customer("Jasper"). customer("Frank"). waiter(w). food("roast beef"). beverage("coffee"). st_hpd(order("Jasper", "roast beef", w), true, 0). st_hpd(order("Jasper", "coffee", w), true, 0). st_hpd(put_down(w, "coffee", t), true, 1). st_hpd(put_down(w, "roast beef", t), true, 1). st_hpd(eat("Jasper", "roast beef"), true, 2). st_hpd(drink("Jasper", "coffee"), true, 2). st_hpd(eat("Frank", "roast beef"), true, 2). st_hpd(drink("Frank", "coffee"), true, 2). st_hpd(pay("Jasper", b), false). st_hpd(pay("Frank", b), true, 3).
```

### Ground Truth
```clingo
restaurant("a restaurant"). customer(they). member("Jasper", they). member("Frank", they). food(f). member("roast beef", f). member(coffee, f). waiter(w). story_step(0..4). st_hpd(enter(they, "a restaurant"), true, 0). st_hpd(order_for("Jasper", they, f, w), true, 1). st_hpd(put_down(w, f, t), true, 2). st_hpd(eat(they, f), true, 3). st_hpd(pay("Jasper", b), false, 4). st_hpd(pay("Frank", b), true, 4).
```

---

## Story #79 — Partial Match (Similarity: 0.0769)

**Story:** [REDACTED — original ROCStories text; storyid=845b62e4-9240-4afe-8d59-ae2bc183967c]

### Predicted
```clingo
restaurant("steakhouse"). customer("The couple"). food("steaks"). waiter(w). st_hpd(eat("The couple", "steaks"), true, 0). st_hpd(put_down(w, b, t), true, 1). st_hpd(read_bill("The couple"), true, 2).
```

### Ground Truth
```clingo
restaurant("new steakhouse"). customer("the couple"). food("huge cuts of meat"). st_obs(in("the couple", "new steakhouse"), true, 0). st_hpd(put_down(w, "huge cuts of meat", t), true, 1). st_hpd(eat("the couple", "huge cuts of meat"), true, 2). st_hpd(put_down(w, b, t), true, 3).
```

---

## Story #34 — Partial Match (Similarity: 0.0909)

**Story:** One day, Andy felt hungry and went to the RRGrill restaurant for dinner. The restaurant was open, but there was no table available for Andy. Andy decided to wait. A table became available soon after.

### Predicted
```clingo
restaurant("RRGrill restaurant"). customer("Andy"). st_hpd(enter("Andy", "RRGrill restaurant"), true, 0). st_obs(open("RRGrill restaurant"), true, 1). st_obs(available(t, "RRGrill restaurant"), false, 1). st_obs(available(t, "RRGrill restaurant"), true, 2).
```

### Ground Truth
```clingo
restaurant("RRGrill"). customer("Andy"). story_step(0..2). st_hpd(enter("Andy", "RRGrill"), true, 0). st_obs(table_available, false, 1). st_hpd(wait("Andy"), true, 1). st_hpd(free_table, true, 2).
```

---

## Story #45 — Partial Match (Similarity: 0.1000)

**Story:** The restaurant was very busy. A group of friends was seated, but no waiter came to take their order. After waiting for twenty minutes, they decided to leave and go somewhere else.

### Predicted
```clingo
restaurant("restaurant"). customer(they). st_obs(sitting(they), true, 0). st_hpd(order(they), false, 1). st_hpd(leave(they), true, 2).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer("group of friends"). waiter(w). story_step(0..2). st_obs(sitting("group of friends"), true, 0). st_hpd(served("group of friends"), false). st_hpd(leave("group of friends"), true, 1).
```

---

## Story #38 — Partial Match (Similarity: 0.1176)

**Story:** One day, Andy felt hungry and went to the RRGrill restaurant for dinner. The restaurant was open and the waiter led Andy to a table. Andy went through the whole menu, but he didn't find any dish that he liked. Andy decided to leave.

### Predicted
```clingo
restaurant("RRGrill restaurant"). customer("Andy"). waiter("the waiter"). st_obs(open("RRGrill restaurant"), true, 0). st_hpd(enter("Andy", "RRGrill restaurant"), true, 1). st_hpd(lead_to("the waiter", "Andy", t), true, 2). st_hpd(read_menu("Andy"), true, 3). st_hpd(order("Andy"), false, 4). st_hpd(leave("Andy"), true, 5).
```

### Ground Truth
```clingo
restaurant("RRGrill"). customer("Andy"). food("nothing"). waiter("the waiter"). story_step(0..4). st_hpd(enter("Andy", "RRGrill"), true, 0). st_hpd(lead_to("the waiter", "Andy", t), true, 1). st_hpd(put_down("Andy", m, t), true, 2). st_stop_activity("Andy", 3). next_st(2, 3). st_hpd(leave("Andy"), true, 4).
```

---

## Story #33 — Partial Match (Similarity: 0.1250)

**Story:** One day, Andy felt hungry and went to the RRGrill restaurant for dinner. The restaurant was open, but there was no table available for Andy.

### Predicted
```clingo
restaurant("RRGrill restaurant"). customer("Andy"). st_hpd(enter("Andy", "RRGrill restaurant"), true, 0). st_obs(open("RRGrill restaurant"), true, 1). st_obs(available(t, "RRGrill restaurant"), false, 1).
```

### Ground Truth
```clingo
restaurant("RRGrill"). customer("Andy"). story_step(0..1). st_hpd(enter("Andy", "RRGrill"), true, 0). st_obs(table_available, false, 1).
```

---

## Story #37 — Partial Match (Similarity: 0.1250)

**Story:** One day, Andy felt hungry and went to the RRGrill restaurant for dinner. The restaurant was closed that day. He decided to go to Happy Pizza instead.

### Predicted
```clingo
restaurant("RRGrill restaurant"). customer("Andy"). st_obs(open("RRGrill restaurant"), false, 0).
```

### Ground Truth
```clingo
restaurant("RRGrill"). restaurant("Happy Pizza"). customer("Andy"). story_step(0..2). st_obs(closed("RRGrill"), true, 0). stop_activity("Andy", 1). st_hpd(move("Andy", "RRGrill", "Happy Pizza"), true, 2).
```

---

## Story #61 — Partial Match (Similarity: 0.1250)

**Story:** The book club members met at the quiet cafe. They ordered various teas and pastries. Everyone enjoyed their selections while discussing the latest novel.

### Predicted
```clingo
restaurant("quiet cafe"). customer(they). beverage("various teas"). food("pastries"). st_obs(in(they, "quiet cafe"), true, 0). st_hpd(order(they, "various teas", w), true, 1). st_hpd(order(they, "pastries", w), true, 1). st_hpd(drink(they, "various teas"), true, 2). st_hpd(eat(they, "pastries"), true, 2).
```

### Ground Truth
```clingo
restaurant("quiet cafe"). customer("book club members"). food("pastries"). beverage("teas"). story_step(0..2). st_hpd(enter("book club members", "quiet cafe"), true, 0). st_hpd(order("book club members", "pastries", "the waiter"), true, 1). st_hpd(order("book club members", "teas", "the waiter"), true, 1). st_hpd(eat("book club members", "pastries"), true, 2). st_hpd(drink("book club members", "teas"), true, 2).
```

---

## Story #80 — Partial Match (Similarity: 0.1304)

**Story:** [REDACTED — original ROCStories text; storyid=d85b7ce5-0d84-4181-afe4-52c64711145a]

### Predicted
```clingo
restaurant("Genki Ya"). customer("I"). customer("son"). member("I", they). member("son", they). beverage("Japanese beers"). food("fish roe"). food("two combo sashimi-sushi dishes"). waiter(w). st_hpd(enter(they, "Genki Ya"), true, 0). st_hpd(drink(they, "Japanese beers"), true, 1). st_hpd(eat(they, "fish roe"), true, 1). st_hpd(eat(they, "two combo sashimi-sushi dishes"), true, 1).
```

### Ground Truth
```clingo
restaurant("Genki Ya"). customer(we). person("my son"). person("I"). member("my son", we). member("I", we). beverage("japanese beers"). food(f). member("fish roe", f). member("sashimi-sushi dishes", f). st_hpd(enter(we, "Genki Ya"), true, 0). st_hpd(eat(we, f), true, 2). st_hpd(drink(we, "japanese beers"), true, 2).
```

---

## Story #39 — Partial Match (Similarity: 0.1333)

**Story:** One day, Andy felt hungry and went to the RRGrill restaurant for dinner. The restaurant was open. The waiter led him to a table. As Andy was sitting down before having a chance to order, he received an emergency phone call and had to leave.

### Predicted
```clingo
restaurant("RRGrill restaurant"). customer("Andy"). waiter("The waiter"). st_obs(open("RRGrill restaurant"), true, 0). st_hpd(enter("Andy", "RRGrill restaurant"), true, 1). st_hpd(lead_to("The waiter", "Andy", t), true, 2). st_hpd(sit("Andy"), true, 3). st_hpd(order("Andy"), false, 4). st_hpd(leave("Andy"), true, 5).
```

### Ground Truth
```clingo
restaurant("RRGrill"). customer("Andy"). waiter("the waiter"). story_step(0..3). st_hpd(enter("Andy", "RRGrill"), true, 0). st_hpd(lead_to("the waiter", "Andy", t), true, 1). st_obs(sitting("Andy"), true, 2). st_stop_activity("Andy", 2). st_hpd(leave("Andy"), true, 3).
```

---

## Story #28 — Partial Match (Similarity: 0.1500)

**Story:** One day, Andy felt hungry, and went to the RRGrill restaurant for dinner. The restaurant was open, so he walked into the restaurant where he was greeted by the waiter and was led to the table. Andy ordered soup and he ate it with pleasure. He paid cash and left.

### Predicted
```clingo
restaurant("RRGrill restaurant"). customer("Andy"). waiter("the waiter"). food("soup"). st_obs(open("RRGrill restaurant"), true, 0). st_hpd(enter("Andy", "RRGrill restaurant"), true, 1). st_hpd(greet("the waiter", "Andy"), true, 2). st_hpd(lead_to("the waiter", "Andy", t), true, 3). st_hpd(order("Andy", "soup", "the waiter"), true, 4). st_hpd(eat("Andy", "soup"), true, 5). st_hpd(pay("Andy", b), true, 6). st_hpd(leave("Andy"), true, 7).
```

### Ground Truth
```clingo
restaurant("RRGrill"). customer(andy). food(soup). waiter("the waiter"). story_step(0..4). st_hpd(enter(andy, "RRGrill"), true, 0). st_hpd(greet("the waiter", andy), true, 1). st_hpd(lead_to("the waiter", andy, t), true, 2). st_hpd(order(andy, soup, "the waiter"), true, 3). st_hpd(eat(andy, soup), true, 4). st_hpd(pay(andy, b), true, 5). st_hpd(leave(andy), true, 6).
```

---

## Story #76 — Partial Match (Similarity: 0.1538)

**Story:** [REDACTED — original ROCStories text; storyid=6ead4a09-8e5f-4fbc-8a32-b706bdbb7a87]

### Predicted
```clingo
restaurant("Allston Diner"). customer(they). food("breakfast meals"). waiter(w). st_hpd(enter(they, "Allston Diner"), true, 0). st_hpd(eat(they, "breakfast meals"), true, 1).
```

### Ground Truth
```clingo
restaurant("Allston Diner"). customer(we). person("our son"). customer("a friend"). member("our son", we). food("breakfast meals"). st_hpd(enter(we, "Allston Diner"), true, 0). st_hpd(eat(we, "breakfast meals"), true, 1). st_hpd(eat("a friend", "breakfast meals"), true, 1).
```

---

## Story #93 — Partial Match (Similarity: 0.1667)

**Story:** [REDACTED — original ROCStories text; storyid=0b8e4ddd-6ada-42ba-9d6f-508db0bac85a]

### Predicted
```clingo
restaurant("restaurant"). customer("I"). customer("mother"). food("steak"). waiter(w). st_hpd(enter("I", "restaurant"), true, 0). st_obs(sitting("I"), true, 1). st_hpd(order("I", "steak", w), true, 2). st_obs(available("steak", "restaurant"), false, 3). st_hpd(leave("I"), true, 4).
```

### Ground Truth
```clingo
restaurant("the restaurant"). restaurant("Burger King"). customer(we). person("I"). person("my mother"). food("steak"). st_hpd(sit(we), true, 0). st_hpd(order("I", "steak", w), true, 1). st_obs(available("steak", "the restaurant"), false, 1). st_hpd(leave(we), true, 2). st_hpd(enter(we, "Burger King"), true, 3).
```

---

## Story #19 — Partial Match (Similarity: 0.1786)

**Story:** Brand sat in a chair. He picked up the menu and ordered a whiskey with Pepsi, but no ice. Pyrogies and sausage cooked in sauerkraut, he told the waiter. The waiter brought Brand his drink. Then, the waiter placed the food on the table. Brand asked the waiter to bring him a large bowl of borscht when he was done with the pyrogies and sausage. The waiter went back into the kitchen. Brand ate the pyrogies and then the sausage and sauerkraut. Then, the waiter brought out Brand's bowl of soup.

### Predicted
```clingo
restaurant(r). customer("Brand"). waiter("the waiter"). beverage("whiskey with Pepsi, but no ice"). food("Pyrogies and sausage cooked in sauerkraut"). food("large bowl of borscht"). st_hpd(sit("Brand"), true, 0). st_hpd(pick_up("Brand", m, t), true, 1). st_hpd(order("Brand", "whiskey with Pepsi, but no ice", "the waiter"), true, 2). st_hpd(order("Brand", "Pyrogies and sausage cooked in sauerkraut", "the waiter"), true, 2). st_hpd(put_down("the waiter", "whiskey with Pepsi, but no ice", t), true, 3). st_hpd(put_down("the waiter", "Pyrogies and sausage cooked in sauerkraut", t), true, 4). st_hpd(request("Brand", "large bowl of borscht", "the waiter"), true, 5). st_hpd(eat("Brand", "Pyrogies and sausage cooked in sauerkraut"), true, 6). st_hpd(put_down("the waiter", "large bowl of borscht", t), true, 7).
```

### Ground Truth
```clingo
restaurant(r). customer("Brand"). beverage("whiskey with Pepsi, no ice"). food(f). member(pyrogies, f). member("sausage in sauerkraut", f). food(borscht). waiter("the waiter"). story_step(0..9). st_hpd(sit("Brand"), true, 0). st_hpd(pick_up("Brand", m, t), true, 1). st_hpd(order("Brand", "whiskey with Pepsi, no ice", "the waiter"), true, 2). st_hpd(order("Brand", f, "the waiter"), true, 3). st_hpd(put_down("the waiter", "whiskey with Pepsi, no ice"), t), true, 4). st_hpd(put_down("the waiter", f, t), true, 5). st_hpd(order("Brand", borscht, "the waiter"), true, 6). st_hpd(move("the waiter", t, kitchen), true, 7). st_hpd(eat("Brand", f), true, 8). st_hpd(put_down("the waiter", borscht, t), true, 9).
```

---

## Story #78 — Partial Match (Similarity: 0.1818)

**Story:** [REDACTED — original ROCStories text; storyid=02fbf49d-54f4-493d-b4af-609cc1e23a22]

### Predicted
```clingo
restaurant("diner"). customer("Betsy"). food("pancakes"). food("bacon"). beverage("coffee"). waiter("The waitress"). st_obs(in("Betsy", "diner"), true, 0). st_hpd(order("Betsy", "pancakes", "The waitress"), true, 1). st_hpd(order("Betsy", "bacon", "The waitress"), true, 1). st_hpd(order("Betsy", "coffee", "The waitress"), true, 1). st_hpd(eat("Betsy", "pancakes"), true, 2). st_hpd(eat("Betsy", "bacon"), true, 2). st_hpd(drink("Betsy", "coffee"), true, 2). st_hpd(pay("Betsy", tip), true, 3).
```

### Ground Truth
```clingo
restaurant("a diner"). customer("Betsy"). food(f). member("pancakes", f). member("bacon", f). beverage("coffee"). waiter("the waitress"). st_hpd(order("Betsy", f, "the waitress"), true, 0). st_hpd(order("Betsy", "coffee", "the waitress"), true, 0). st_hpd(eat("Betsy", f), true, 1). st_hpd(drink("Betsy", "coffee"), true, 1). st_hpd(pay("Betsy", tip), true, 2).
```

---

## Story #17 — Partial Match (Similarity: 0.2000)

**Story:** The waiter brought his dinner. He was eating something spotted with eggs and livers. He finished but the waiter wouldn't come total the bill.

### Predicted
```clingo
customer("He"). waiter("the waiter"). food("dinner"). st_hpd(put_down("the waiter", "dinner", t), true, 0). st_hpd(eat("He", "dinner"), true, 1). st_hpd(pay("He", b), false).
```

### Ground Truth
```clingo
customer("he"). food("something spotted with eggs and livers"). waiter("the waiter"). story_step(0..1). st_hpd(put_down("the waiter", "something spotted with eggs and livers", t), true, 0). st_hpd(eat("he", "something spotted with eggs and livers"), true, 1). st_hpd(put_down("the waiter", b, t), false).
```

---

## Story #64 — Partial Match (Similarity: 0.2000)

**Story:** Penny booked a table for two. She and her friend arrived at the restaurant and were seated immediately. They perused the menu, ordered their food, and had a lovely meal.

### Predicted
```clingo
restaurant("restaurant"). customer("Penny"). customer("friend"). member("Penny", they). member("friend", they). food(f). waiter(w). st_hpd(enter(they, "restaurant"), true, 0). st_obs(sitting(they), true, 1). st_hpd(read_menu(they), true, 2). st_hpd(order(they, f, w), true, 3). st_hpd(eat(they, f), true, 4).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer(they). person("Penny"). person("her friend"). member("Penny", they). member("her friend", they). food("food"). story_step(0..5). st_hpd(enter(they, "the restaurant"), true, 0). st_hpd(sit(they), true, 1). st_hpd(read_menu(they), true, 3). st_hpd(order(they, "food", w), true, 4). st_hpd(eat(they, "food"), true, 5).
```

---

## Story #89 — Partial Match (Similarity: 0.2000)

**Story:** [REDACTED — original ROCStories text; storyid=c93ca5db-716f-4572-868e-bd22aa4a9018]

### Predicted
```clingo
restaurant("Genki Ya"). customer("me"). customer("son"). member("me", they). member("son", they). food("sashimi"). waiter(w). st_hpd(enter(they, "Genki Ya"), true, 0). st_hpd(eat(they, "sashimi"), true, 1).
```

### Ground Truth
```clingo
restaurant("Genki Ya"). customer(we). person("my son"). person("me"). member("my son", we). member("me", we). food("sashimi"). st_hpd(enter(we, "Genki Ya"), true, 0). st_hpd(eat(we, "sashimi"), true, 1).
```

---

## Story #52 — Partial Match (Similarity: 0.2105)

**Story:** David walked into the seafood restaurant and was shown to his table. He browsed the menu and ordered grilled salmon with vegetables. The food arrived quickly. David ate his meal and paid the bill before leaving.

### Predicted
```clingo
restaurant("seafood restaurant"). customer("David"). food("grilled salmon with vegetables"). waiter(w). st_hpd(enter("David", "seafood restaurant"), true, 0). st_hpd(lead_to(w, "David", t), true, 1). st_hpd(read_menu("David"), true, 2). st_hpd(order("David", "grilled salmon with vegetables", w), true, 3). st_hpd(put_down(w, "grilled salmon with vegetables", t), true, 4). st_hpd(eat("David", "grilled salmon with vegetables"), true, 5). st_hpd(pay("David", b), true, 6). st_hpd(leave("David"), true, 7).
```

### Ground Truth
```clingo
restaurant("seafood restaurant"). customer("David"). food("grilled salmon with vegetables"). waiter("the waiter"). st_hpd(enter("David", "seafood restaurant"), true, 0). st_hpd(lead_to("the waiter", "David", t), true, 1). st_hpd(order("David", "grilled salmon with vegetables", "the waiter"), true, 2). st_hpd(put_down("the waiter", "grilled salmon with vegetables", t), true, 3). st_hpd(eat("David", "grilled salmon with vegetables"), true, 4). st_hpd(pay("David", b), true, 5). st_hpd(leave("David"), true, 6).
```

---

## Story #84 — Partial Match (Similarity: 0.2143)

**Story:** [REDACTED — original ROCStories text; storyid=0f9b69ff-6fbe-4e94-a37a-8ef3fbf2a876]

### Predicted
```clingo
restaurant("diner"). customer("Donna"). food("cheeseburger"). food("onion rings"). waiter(w). st_hpd(enter("Donna", "diner"), true, 0). st_hpd(order("Donna", "cheeseburger", w), true, 1). st_hpd(order("Donna", "onion rings", w), true, 1). st_hpd(eat("Donna", "cheeseburger"), true, 2).
```

### Ground Truth
```clingo
restaurant("diner"). customer("Donna"). food(f). member("cheeseburger", f). member("onion rings", f). st_hpd(enter("Donna", "diner"), true, 0). st_hpd(order("Donna", f, w), true, 1). st_hpd(eat("Donna", f), true, 2).
```

---

## Story #36 — Partial Match (Similarity: 0.2308)

**Story:** One day, Andy felt hungry and went to the RRGrill restaurant for dinner. The restaurant was open and Tom, Andyâ€™s friend, had his birthday party in there. Tom had prepaid for all the food that was offered. The waiter led Andy to Tomâ€™s table. Andy joined the party.

### Predicted
```clingo
restaurant("RRGrill restaurant"). customer("Andy"). customer("Tom"). waiter("The waiter"). st_obs(open("RRGrill restaurant"), true, 0). st_hpd(enter("Andy", "RRGrill restaurant"), true, 1). st_hpd(lead_to("The waiter", "Andy", t), true, 2).
```

### Ground Truth
```clingo
restaurant("RRGrill"). customer("Andy"). person("Tom"). food("all the food"). waiter("the waiter"). story_step(0..2). st_hpd(enter("Andy", "RRGrill"), true, 0). st_hpd(lead_to("the waiter", "Andy", t), true, 1). st_obs(informed("the waiter", "all the food", "Andy"), true, 2). st_hpd(pay("Tom", b), 2).
```

---

## Story #97 — Partial Match (Similarity: 0.2308)

**Story:** [REDACTED — original ROCStories text; storyid=d25ec012-9f9f-48e6-8274-e6ac4a4b59e4]

### Predicted
```clingo
restaurant("restaurant"). customer("Tim"). food(f). waiter("The waiter"). st_obs(in("Tim", "restaurant"), true, 0). st_hpd(put_down("The waiter", f, t), true, 1). st_hpd(complain("Tim", "The waiter"), true, 2).
```

### Ground Truth
```clingo
restaurant(r). customer("Tim"). food("wrong order"). waiter("the waiter"). st_obs(in("Tim", r), true, 0). st_hpd(put_down("the waiter", "wrong order", t), true, 1). st_hpd(complain("Tim", "the waiter"), true, 2). st_next(1, 2). st_hpd(put_down("the waiter", f, t), true, 3).
```

---

## Story #29 — Partial Match (Similarity: 0.2353)

**Story:** Nicole went to a vegetarian restaurant. She ordered lentil soup. When the waitress brought her the soup, she told Nicole that it was on the house. Nicole enjoyed the soup and then left.

### Predicted
```clingo
restaurant("vegetarian restaurant"). customer("Nicole"). food("lentil soup"). waiter("the waitress"). st_hpd(enter("Nicole", "vegetarian restaurant"), true, 0). st_hpd(order("Nicole", "lentil soup", "the waitress"), true, 1). st_hpd(put_down("the waitress", "lentil soup", t), true, 2). st_hpd(pay("Nicole", b), false). st_hpd(eat("Nicole", "lentil soup"), true, 3). st_hpd(leave("Nicole"), true, 4).
```

### Ground Truth
```clingo
restaurant(veg_r). customer(nicole). person(owner). food(lentil_soup). waiter(waitress). story_step(0..5). st_hpd(enter(nicole, veg_r), true, 0). st_hpd(order(nicole, lentil_soup, waitress), true, 1). st_hpd(pay(owner, b), true, 2). st_hpd(put_down(waitress, lentil_soup, t), true, 3). st_hpd(eat(nicole, lentil_soup), true, 4). st_hpd(leave(nicole), true, 5).
```

---

## Story #73 — Partial Match (Similarity: 0.2353)

**Story:** David entered the deli and took a seat at the counter. He ordered a pastrami sandwich and a pickle. The cook prepared his sandwich and the server brought it to him. David ate his lunch quickly.

### Predicted
```clingo
restaurant("deli"). customer("David"). food("pastrami sandwich and a pickle"). waiter("the server"). st_hpd(enter("David", "deli"), true, 0). st_hpd(sit("David"), true, 1). st_hpd(order("David", "pastrami sandwich and a pickle", "the server"), true, 2). st_hpd(prepare("The cook", "pastrami sandwich and a pickle", "the server"), true, 3). st_hpd(put_down("the server", "pastrami sandwich and a pickle", t), true, 4). st_hpd(eat("David", "pastrami sandwich and a pickle"), true, 5).
```

### Ground Truth
```clingo
restaurant("the deli"). customer("David"). food(f). member("pastrami sandwich", f). member("pickle", f). st_hpd(enter("David", "the deli"), true, 0). st_hpd(sit("David"), true, 1). st_hpd(order("David", f, "the server"), true, 2). st_hpd(prepare("the cook", f, "the server"), true, 3). st_hpd(put_down("the server", f, t), true, 4). st_hpd(eat("David", f), true, 5).
```

---

## Story #77 — Partial Match (Similarity: 0.2353)

**Story:** [REDACTED — original ROCStories text; storyid=44b80dab-a351-4065-86b8-43d519dff470]

### Predicted
```clingo
restaurant("new restaurant"). customer("Karl"). customer("wife"). member("Karl", they). member("wife", they). waiter("the waiter"). st_hpd(enter(they, "new restaurant"), true, 0). st_obs(sitting(they), true, 1). st_obs(served(they), false, 2). st_hpd(leave(they), true, 3).
```

### Ground Truth
```clingo
restaurant("new restaurant"). waiter("the waiter"). customer(they). person("Karl"). person("his wife"). member("Karl", they). member("his wife", they). waiter(w). st_obs(sitting(they), true, 0). st_hpd(served(they), false, 1). st_hpd(leave(they), true, 2).
```

---

## Story #65 — Partial Match (Similarity: 0.2400)

**Story:** Maria entered the Italian restaurant and was greeted by the host. She was seated at a corner table and handed a menu. Maria ordered spaghetti carbonara and a glass of red wine. The waiter brought her order promptly. She enjoyed her meal and asked for the bill.

### Predicted
```clingo
restaurant("Italian restaurant"). customer("Maria"). food("spaghetti carbonara"). beverage("glass of red wine"). waiter("The waiter"). st_hpd(enter("Maria", "Italian restaurant"), true, 0). st_hpd(greet("the host", "Maria"), true, 1). st_obs(sitting("Maria"), true, 2). st_hpd(put_down("the host", m, t), true, 3). st_hpd(order("Maria", "spaghetti carbonara", "The waiter"), true, 4). st_hpd(order("Maria", "glass of red wine", "The waiter"), true, 4). st_hpd(put_down("The waiter", "spaghetti carbonara", t), true, 5). st_hpd(put_down("The waiter", "glass of red wine", t), true, 5). st_hpd(eat("Maria", "spaghetti carbonara"), true, 6). st_hpd(request("Maria", b, "The waiter"), true, 7).
```

### Ground Truth
```clingo
restaurant("Italian restaurant"). customer("Maria"). person("the host"). food("spaghetti carbonara"). beverage("red wine"). waiter("the waiter"). story_step(0..6). st_hpd(enter("Maria", "Italian restaurant"), true, 0). st_hpd(greet("the host", "Maria"), true, 1). st_hpd(lead_to("the host", "Maria", t), true, 2). st_hpd(order("Maria", "spaghetti carbonara", "the waiter"), true, 3). st_hpd(order("Maria", "red wine", "the waiter"), true, 3). st_hpd(put_down("the waiter", "spaghetti carbonara", t), true, 4). st_hpd(put_down("the waiter", "red wine", t), true, 4). st_hpd(eat("Maria", "spaghetti carbonara"), true, 5). st_hpd(drink("Maria", "red wine"), true, 5). st_hpd(request("Maria", b, "the waiter"), true, 6).
```

---

## Story #21 — Partial Match (Similarity: 0.2500)

**Story:** The waiter brought the wine to their table. Then, Emanuel studied the menu. He ordered the gypsy shashlik for Ingrid and himself. After the waiter left, they drank the wine. The waiter brought the shashlik to their table.

### Predicted
```clingo
restaurant(r). customer("Emanuel"). customer("Ingrid"). waiter("the waiter"). food("gypsy shashlik"). beverage("wine"). st_hpd(put_down("the waiter", "wine", t), true, 0). st_hpd(read_menu("Emanuel"), true, 1). st_hpd(order("Emanuel", "gypsy shashlik", "the waiter"), true, 2). st_hpd(drink("Emanuel", "wine"), true, 3). st_hpd(drink("Ingrid", "wine"), true, 3). st_hpd(put_down("the waiter", "gypsy shashlik", t), true, 4).
```

### Ground Truth
```clingo
restaurant(r). customer(they). member("Emanuel"). member("Ingrid"). beverage(wine). food("gypsy shashlik"). waiter("the waiter"). story_step(0..5). st_hpd(put_down("the waiter", wine, t), true, 0). st_hpd(pick_up("Emanuel", m, t), true, 1). st_hpd(order_for("Emanuel", they, "gypsy shashlik", "the waiter"), true, 2). st_hpd(move("the waiter", t, kitchen), true, 3). st_hpd(drink(they, wine), true, 4). st_hpd(put_down("the waiter", "gypsy shashlik", t), true, 5).
```

---

## Story #40 — Partial Match (Similarity: 0.2500)

**Story:** Ken was at a sushi restaurant. He ordered the tuna roll. The waiter brought the tuna roll, but Ken noticed a long hair in it. He complained to the waiter, who apologized and brought a new, hair-free roll.

### Predicted
```clingo
restaurant("sushi restaurant"). customer("Ken"). food("tuna roll"). food("new, hair-free roll"). waiter("The waiter"). st_obs(in("Ken", "sushi restaurant"), true, 0). st_hpd(order("Ken", "tuna roll", "The waiter"), true, 1). st_hpd(put_down("The waiter", "tuna roll", t), true, 2). st_hpd(complain("Ken", "The waiter"), true, 3). st_hpd(put_down("The waiter", "new, hair-free roll", t), true, 4).
```

### Ground Truth
```clingo
restaurant("sushi restaurant"). customer("Ken"). food("tuna roll"). food("new tuna roll"). waiter("the waiter"). story_step(0..4). st_hpd(order("Ken", "tuna roll", "the waiter"), true, 0). st_hpd(put_down("the waiter", "tuna roll", t), true, 1). st_hpd(complain("Ken", "the waiter"), true, 2). st_next(1, 2). st_hpd(put_down(w, "new tuna roll", t), true, 3).
```

---

## Story #87 — Partial Match (Similarity: 0.2500)

**Story:** [REDACTED — original ROCStories text; storyid=7dc0c96f-dd24-4561-9a4f-bd1b6b3ca520]

### Predicted
```clingo
restaurant("restaurant"). customer("I"). food(f). waiter(w). st_hpd(enter("I", "restaurant"), true, 0). st_hpd(put_down(w, f, t), true, 1). st_hpd(complain("I", w), true, 2).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer("I"). food("wrong order"). st_hpd(enter("I", "the restaurant"), true, 0). st_hpd(order("I", f, w), true, 1). st_hpd(put_down(w, "wrong order", t), true, 2). st_hpd(request("I", pick_up(w, "burnt pizza", t), w), true, 3). st_next(2,3).
```

---

## Story #96 — Partial Match (Similarity: 0.2500)

**Story:** [REDACTED — original ROCStories text; storyid=77710d2a-dbc2-4c99-a892-190b529ad219]

### Predicted
```clingo
restaurant("fast food restaurant"). customer("Dina"). customer("friend"). member("Dina", they). member("friend", they). food("order of fries"). waiter(w). st_obs(in(they, "fast food restaurant"), true, 0). st_hpd(order(they, "order of fries", w), true, 1). st_hpd(pay("Dina", b), true, 2). st_hpd(pay("friend", b), true, 2). st_hpd(eat("Dina", "order of fries"), true, 3).
```

### Ground Truth
```clingo
restaurant("fast food restaurant"). customer(they). person("Dina"). person("a friend"). member("Dina", they). member("a friend", they). food("fries"). st_obs(in("Dina", "fast food restaurant"), true, 0). st_obs(hungry("Dina"), false, 1). st_hpd(order(they, "fries", w), true, 2). st_hpd(pay("Dina", b), true, 3). st_hpd(pay("a friend", b), true, 3). st_hpd(eat("Dina", "fries"), true, 4).
```

---

## Story #98 — Partial Match (Similarity: 0.2500)

**Story:** [REDACTED — original ROCStories text; storyid=09a69527-2433-4e12-9943-9dcacbdf9b04]

### Predicted
```clingo
restaurant("new place"). customer("Joe"). food("meal"). waiter(w). st_hpd(enter("Joe", "new place"), true, 0). st_hpd(order("Joe", "meal", w), true, 1). st_hpd(eat("Joe", "meal"), true, 2).
```

### Ground Truth
```clingo
restaurant("new place"). customer("Joe"). food("a meal"). st_obs(hungry("Joe"), true, 0). st_hpd(enter("Joe", "new place"), true, 1). st_hpd(order("Joe", "a meal", w), true, 2). st_hpd(eat("Joe", "a meal"), true, 3). st_obs(hungry("Joe"), false, 4).
```

---

## Story #27 — Partial Match (Similarity: 0.2632)

**Story:** Nicole and Sam went to a vegetarian restaurant. She ordered a lentil soup. He ordered a miso soup. They both enjoyed their soups.

### Predicted
```clingo
restaurant("vegetarian restaurant"). customer("Nicole"). customer("Sam"). food("lentil soup"). food("miso soup"). waiter(w). st_hpd(enter("Nicole", "vegetarian restaurant"), true, 0). st_hpd(enter("Sam", "vegetarian restaurant"), true, 0). st_hpd(order("Nicole", "lentil soup", w), true, 1). st_hpd(order("Sam", "miso soup", w), true, 1). st_hpd(eat("Nicole", "lentil soup"), true, 2). st_hpd(eat("Sam", "miso soup"), true, 2).
```

### Ground Truth
```clingo
restaurant(veg_r). customer(nicole). customer(sam). food(lentil_soup). food(miso_soup). waiter(w). story_step(0..3). st_hpd(enter(nicole, veg_r), true, 0). st_hpd(enter(sam, veg_r), true, 0). st_hpd(order(nicole, lentil_soup, waitress), true, 1). st_hpd(order(sam, miso_soup, waitress), true, 2). st_hpd(eat(nicole, lentil_soup), true, 3). st_hpd(eat(sam, miso_soup), true, 3).
```

---

## Story #47 — Partial Match (Similarity: 0.2667)

**Story:** Gary went to a restaurant for his birthday. He ordered a steak. After he finished eating, the waiter surprised him with a small cake, on the house. Gary left a large tip.

### Predicted
```clingo
restaurant("restaurant"). customer("Gary"). food("steak"). food("small cake"). waiter("the waiter"). st_hpd(enter("Gary", "restaurant"), true, 0). st_hpd(order("Gary", "steak", "the waiter"), true, 1). st_hpd(eat("Gary", "steak"), true, 2). st_hpd(put_down("the waiter", "small cake", t), true, 3). st_hpd(pay("Gary", tip), true, 4).
```

### Ground Truth
```clingo
restaurant("a restaurant"). customer("Gary"). food("steak"). food("cake"). waiter("the waiter"). story_step(0..3). st_hpd(order("Gary", "steak", "the waiter"), true, 0). st_hpd(eat("Gary", "steak"), true, 1). st_hpd(put_down("the waiter", "cake", t), true, 2). st_hpd(pay("Gary", tip), true, 3).
```

---

## Story #53 — Partial Match (Similarity: 0.2759)

**Story:** The Johnson family entered the family restaurant. They were seated in a booth and given menus. Mr. Johnson ordered steak, Mrs. Johnson ordered salad, and their son ordered pizza. The waiter brought all their orders together.

### Predicted
```clingo
restaurant("family restaurant"). customer("Mr. Johnson"). customer("Mrs. Johnson"). customer("son"). food("steak"). food("salad"). food("pizza"). waiter("The waiter"). st_hpd(enter(they, "family restaurant"), true, 0). st_obs(sitting(they), true, 1). st_hpd(pick_up(they, m, t), true, 2). st_hpd(order("Mr. Johnson", "steak", "The waiter"), true, 3). st_hpd(order("Mrs. Johnson", "salad", "The waiter"), true, 3). st_hpd(order("son", "pizza", "The waiter"), true, 3). st_hpd(put_down("The waiter", "steak", t), true, 4). st_hpd(put_down("The waiter", "salad", t), true, 4). st_hpd(put_down("The waiter", "pizza", t), true, 4).
```

### Ground Truth
```clingo
restaurant("family restaurant"). person("Mr. Johnson"). person("Mrs. Johnson"). person("son"). customer("Johnson family"). member("Mr. Johnson", "Johnson family"). member("Mrs. Johnson", "Johnson family"). member("son", "Johnson family"). food("steak"). food("salad"). food("pizza"). waiter("the waiter"). story_step(0..4). st_hpd(enter("Johnson family", "family restaurant"), true, 0). st_obs(sitting("Johnson family"), true, 1). st_hpd(order("Mr. Johnson", "steak", "the waiter"), true, 2). st_hpd(order("Mrs. Johnson", "salad", "the waiter"), true, 2). st_hpd(order("son", "pizza", "the waiter"), true, 2). st_hpd(put_down("the waiter", "steak", t), true, 3). st_hpd(put_down("the waiter", "salad", t), true, 3). st_hpd(put_down("the waiter", "pizza", t), true, 3).
```

---

## Story #20 — Partial Match (Similarity: 0.2857)

**Story:** The waiter brought out escargot for Molly and me. Then the waiter brought out twelve oysters and twelve clams. We shared the clams and oysters. The waiter poured wine for us.

### Predicted
```clingo
restaurant(r). customer("Molly"). customer("me"). member("Molly", they). member("me", they). waiter("the waiter"). food("escargot"). food("twelve oysters and twelve clams"). beverage("wine"). st_hpd(put_down("the waiter", "escargot", t), true, 0). st_hpd(put_down("the waiter", "twelve oysters and twelve clams", t), true, 1). st_hpd(eat(they, "twelve oysters and twelve clams"), true, 2). st_hpd(put_down("the waiter", "wine", t), true, 3).
```

### Ground Truth
```clingo
restaurant(r). customer(we). member("Molly", we). member(me, we). food(escargot). food(f). member("twelve oysters", f). member("twelve clams", f). beverage("wine"). waiter("the waiter"). story_step(0..3). st_hpd(put_down("the waiter", escargot, t), true, 0). st_hpd(put_down("the waiter", f, t), true, 1). st_hpd(eat(we, f), true, 2). st_hpd(put_down("the waiter", wine, t), true, 3).
```

---

## Story #81 — Partial Match (Similarity: 0.2857)

**Story:** [REDACTED — original ROCStories text; storyid=1d235832-c133-4950-ba20-512adb2e3edb]

### Predicted
```clingo
restaurant("Italian restaurant"). customer("Kathy"). customer("friend"). member("Kathy", they). member("friend", they). food("dinner"). waiter(w). st_hpd(enter(they, "Italian restaurant"), true, 0). st_hpd(eat(they, "dinner"), true, 1).
```

### Ground Truth
```clingo
restaurant("new Italian restaurant"). customer(they). person("Kathy"). person("her friend"). member("Kathy", they). member("her friend", they). food("dinner"). st_hpd(enter(they, "new Italian restaurant"), true, 0). st_hpd(eat(they, "dinner"), true, 1).
```

---

## Story #82 — Partial Match (Similarity: 0.3000)

**Story:** [REDACTED — original ROCStories text; storyid=2cf524c3-5e49-4ba9-9590-f84429fbdc01]

### Predicted
```clingo
restaurant("new restaurant"). customer("Elmer"). customer("Emma"). member("Elmer", they). member("Emma", they). food("burgers"). beverage("milkshakes"). food("fries"). waiter(w). st_hpd(enter(they, "new restaurant"), true, 0). st_hpd(order(they, "burgers", w), true, 1). st_hpd(order(they, "milkshakes", w), true, 1). st_hpd(order("Elmer", "fries", w), true, 1).
```

### Ground Truth
```clingo
restaurant("new restaurant"). customer("the couple"). person("Elmer"). person("Emma"). member("Elmer", "the couple"). member("Emma", "the couple"). food("burgers"). food("fries"). beverage("milkshakes"). st_hpd(enter("the couple", "new restaurant"), true, 0). st_hpd(order("the couple", "burgers", w), true, 1). st_hpd(order("the couple", "milkshakes", w), true, 1). st_hpd(order("Elmer", "fries", w), true, 2).
```

---

## Story #67 — Partial Match (Similarity: 0.3077)

**Story:** Maria and Leo entered a quiet Italian restaurant. The waiter seated them at a corner table. They ordered a bottle of red wine. After the waiter brought the wine, they ordered two pasta dishes. They enjoyed their meal, paid the bill, and left.

### Predicted
```clingo
restaurant("Italian restaurant"). customer("Maria"). customer("Leo"). member("Maria", they). member("Leo", they). beverage("bottle of red wine"). food("two pasta dishes"). waiter("The waiter"). st_hpd(enter(they, "Italian restaurant"), true, 0). st_hpd(lead_to("The waiter", they, t), true, 1). st_hpd(order(they, "bottle of red wine", "The waiter"), true, 2). st_hpd(put_down("The waiter", "bottle of red wine", t), true, 3). st_hpd(order(they, "two pasta dishes", "The waiter"), true, 4). st_hpd(eat(they, "two pasta dishes"), true, 5). st_hpd(pay(they, b), true, 6). st_hpd(leave(they), true, 7).
```

### Ground Truth
```clingo
restaurant("quiet Italian restaurant"). customer(they). person("Maria"). person("Leo"). member("Maria", they). member("Leo", they). beverage("red wine"). food("pasta dishes"). waiter("the waiter"). story_step(0..7). st_hpd(enter(they, "quiet Italian restaurant"), true, 0). st_hpd(lead_to("the waiter", they, t), true, 1). st_hpd(order(they, "red wine", "the waiter"), true, 2). st_hpd(put_down("the waiter", "red wine", t), true, 3). st_hpd(order(they, "pasta dishes", "the waiter"), true, 4). st_hpd(eat(they, "pasta dishes"), true, 5). st_hpd(drink(they, "red wine"), true, 5). st_hpd(pay(they, b), true, 6). st_hpd(leave(they), true, 7).
```

---

## Story #35 — Partial Match (Similarity: 0.3333)

**Story:** One day, Andy felt hungry and went to the RRGrill restaurant for dinner. The restaurant was open, but there was no table available for Andy. Andy decided to leave.

### Predicted
```clingo
restaurant("RRGrill"). customer("Andy"). story_step(0..2). st_hpd(enter("Andy", "RRGrill"), true, 0). st_obs(table_available, false, 1). stop_activity("Andy", 1). st_hpd(leave("Andy"), true, 2).
```

### Ground Truth
```clingo
restaurant("RRGrill"). customer("Andy"). story_step(0..3). st_hpd(enter("Andy", "RRGrill"), true, 0). st_hpd(lead_to(w, "Andy", t), false). stop_activity("Andy", 2). st_hpd(leave("Andy"), true, 3).
```

---

## Story #85 — Partial Match (Similarity: 0.3333)

**Story:** [REDACTED — original ROCStories text; storyid=9915e783-6bf9-4d92-9150-b031bf778bb7]

### Predicted
```clingo
restaurant("restaurant"). customer("I"). food("pizza"). waiter(w). st_hpd(enter("I", "restaurant"), true, 0). st_hpd(order("I", "pizza", w), true, 1). st_hpd(put_down(w, "pizza", t), true, 2). st_hpd(complain("I", w), true, 3).
```

### Ground Truth
```clingo
restaurant("a restaurant"). customer("I"). food("pizza"). food("burnt pizza"). st_hpd(enter("I", r), true, 0). st_hpd(order("I", "pizza", w), true, 1). st_hpd(put_down(w, "burnt pizza", t), true, 2). st_hpd(request("I", pick_up(w, "burnt pizza", t), w), true, 3).
```

---

## Story #41 — Partial Match (Similarity: 0.3529)

**Story:** Laura was at a cafe. She ordered a coffee and a croissant. The waiter brought the coffee promptly, but after 30 minutes, the croissant still hadn't arrived. Laura gave up, paid for her coffee, and left.

### Predicted
```clingo
restaurant("cafe"). customer("Laura"). beverage("coffee"). food("croissant"). waiter("The waiter"). st_obs(in("Laura", "cafe"), true, 0). st_hpd(order("Laura", "coffee", "The waiter"), true, 1). st_hpd(order("Laura", "croissant", "The waiter"), true, 1). st_hpd(put_down("The waiter", "coffee", t), true, 2). st_hpd(put_down("The waiter", "croissant", t), false). st_hpd(pay("Laura", "coffee"), true, 3). st_hpd(leave("Laura"), true, 4).
```

### Ground Truth
```clingo
restaurant("cafe"). customer("Laura"). beverage("coffee"). food("croissant").  waiter("the waiter"). story_step(0..4). st_hpd(order("Laura", "coffee", "the waiter"), true, 0). st_hpd(order("Laura", "croissant", "the waiter"), true, 0). st_hpd(put_down("the waiter", "coffee", t), true, 1). st_obs(served("Laura"), false, 2). st_hpd(pay("Laura", b), true, 3). st_hpd(leave("Laura"), true, 4).
```

---

## Story #32 — Partial Match (Similarity: 0.3571)

**Story:** Nicole went to a vegetarian restaurant. She ordered a lentil soup. Nicole was in a hurry, so as soon as the waitress laid the dish on the table, Nicole paid for it in cash and said that she didn't need the bill.

### Predicted
```clingo
restaurant("vegetarian restaurant"). customer("Nicole"). food("lentil soup"). waiter("the waitress"). st_hpd(enter("Nicole", "vegetarian restaurant"), true, 0). st_hpd(order("Nicole", "lentil soup", "the waitress"), true, 1). st_hpd(put_down("the waitress", "lentil soup", t), true, 2). st_hpd(pay("Nicole", b), true, 3). st_obs(bill_generated("Nicole", b), false, 3).
```

### Ground Truth
```clingo
restaurant(veg_r). customer(nicole). person(owner). food(lentil_soup). waiter(waitress). story_step(0..3). st_hpd(enter(nicole, veg_r), true, 0). st_hpd(order(nicole, lentil_soup, waitress), true, 1). st_hpd(put_down(waitress, miso_soup, t), true, 2). st_hpd(pay(nicole, b), true, 3). next_st(2, 3).
```

---

## Story #55 — Partial Match (Similarity: 0.3684)

**Story:** Mark and Lisa went to their favorite sushi restaurant. They were seated at the sushi bar. Mark ordered tuna rolls and Lisa ordered salmon nigiri. The chef prepared their order in front of them.

### Predicted
```clingo
restaurant("sushi restaurant"). customer("Mark"). customer("Lisa"). food("tuna rolls"). food("salmon nigiri"). waiter("The chef"). st_hpd(enter(they, "sushi restaurant"), true, 0). st_obs(sitting(they), true, 1). st_hpd(order("Mark", "tuna rolls", "The chef"), true, 2). st_hpd(order("Lisa", "salmon nigiri", "The chef"), true, 2). st_hpd(prepare("The chef", "tuna rolls", "The chef"), true, 3). st_hpd(prepare("The chef", "salmon nigiri", "The chef"), true, 3).
```

### Ground Truth
```clingo
restaurant("sushi restaurant"). waiter(w). person("Mark"). person("Lisa"). customer("they"). member("Mark", "they"). member("Mark", "they"). food("tuna rolls"). food("salmon nigiri"). story_step(0..4). st_hpd(enter("they", "sushi restaurant"), true, 0). st_obs(sitting("they"), true, 1). st_hpd(order("Mark", "tuna rolls", w), true, 2). st_hpd(order("Lisa", "salmon nigiri", w), true, 2). st_hpd(prepare("the chef", "tuna rolls", w), true, 3). st_hpd(prepare("the chef", "salmon nigiri", w), true, 3).
```

---

## Story #91 — Partial Match (Similarity: 0.3750)

**Story:** [REDACTED — original ROCStories text; storyid=ac7250f9-d416-41bb-aac7-b1dd788b86fb]

### Predicted
```clingo
restaurant("fast food restaurant"). customer("Emily"). food("fries"). food("burger"). waiter("the cashier"). st_obs(in("Emily", "fast food restaurant"), true, 0). st_hpd(order("Emily", "fries", "the cashier"), true, 1). st_hpd(order("Emily", "burger", "the cashier"), true, 1). st_hpd(put_down("the cashier", "burger", t), true, 2). st_hpd(put_down("the cashier", "fries", t), false). st_hpd(complain("Emily", "the cashier"), true, 3).
```

### Ground Truth
```clingo
restaurant("fast food restaurant"). customer("Emily"). food("fries"). food("burger"). waiter("the cashier"). st_hpd(order("Emily", "fries", "the cashier"), true, 0). st_hpd(order("Emily", "burger", "the cashier"), true, 0). st_hpd(put_down("the cashier", "burger", t), true, 1). st_hpd(put_down("the cashier", "fries", t), false). st_hpd(complain("Emily", "the cashier"), true, 2). st_next(1,2).
```

---

## Story #94 — Partial Match (Similarity: 0.3750)

**Story:** [REDACTED — original ROCStories text; storyid=63dfd3a4-930a-4a27-8ed9-60304b6c32f3]

### Predicted
```clingo
restaurant("sushi place"). customer("The couple"). food(f). waiter(w). st_hpd(enter("The couple", "sushi place"), true, 0). st_hpd(eat("The couple", f), true, 1).
```

### Ground Truth
```clingo
restaurant("new sushi place"). customer("The couple"). food(f). st_hpd(enter("The couple", "new sushi place"), true, 0). st_hpd(eat("The couple", f), true, 1).
```

---

## Story #23 — Partial Match (Similarity: 0.3810)

**Story:** I opened the menu and chose the salmon. The waiter poured two glasses of red wine. I sipped the wine. Then our server brought a small plate of hors d'oeuvres. I tried a little bit of everything. Soon, the waiter brought the meal. I tasted the salmon.

### Predicted
```clingo
restaurant(r). customer("I"). waiter("the waiter"). food("salmon"). beverage("red wine"). food("small plate of hors d'oeuvres"). food("meal"). st_hpd(read_menu("I"), true, 0). st_hpd(order("I", "salmon", "the waiter"), true, 1). st_hpd(put_down("the waiter", "red wine", t), true, 2). st_hpd(drink("I", "red wine"), true, 3). st_hpd(put_down("the waiter", "small plate of hors d'oeuvres", t), true, 4). st_hpd(eat("I", "small plate of hors d'oeuvres"), true, 5). st_hpd(put_down("the waiter", "meal", t), true, 6). st_hpd(eat("I", "salmon"), true, 7).
```

### Ground Truth
```clingo
restaurant(r). customer("I"). food(salmon). beverage("red wine"). food("hors d'oeuvres"). waiter("the waiter"). story_step(0..7). st_hpd(pick_up("I", m, t), true, 0). st_hpd(order("I", salmon, "the waiter"), true, 1). st_hpd(put_down("I", "red wine", t), true, 2). st_hpd(drink("I", "red wine"), true, 3). st_hpd(put_down("the waiter", "hors d'oeuvres", t), true, 4). st_hpd(eat("I", "hors d'oeuvres"), true, 5). st_hpd(put_down("the waiter", salmon, t), true, 6). st_hpd(eat("I", salmon), true, 7).
```

---

## Story #44 — Partial Match (Similarity: 0.3846)

**Story:** At an Italian restaurant, Chloe ordered lasagna. The waiter brought her spaghetti instead. Chloe informed the waiter of the mistake.

### Predicted
```clingo
restaurant("Italian restaurant"). customer("Chloe"). food("lasagna"). food("spaghetti"). waiter("The waiter"). st_obs(in("Chloe", "Italian restaurant"), true, 0). st_hpd(order("Chloe", "lasagna", "The waiter"), true, 1). st_hpd(put_down("The waiter", "spaghetti", t), true, 2). st_hpd(complain("Chloe", "The waiter"), true, 3).
```

### Ground Truth
```clingo
restaurant("Italian restaurant"). customer("Chloe"). food("lasagna"). food("spaghetti"). waiter("the waiter"). story_step(0..2). st_hpd(order("Chloe", "lasagna", "the waiter"), true, 0). st_hpd(put_down("the waiter", "spaghetti", t), true, 1). st_hpd(complain("Chloe", "the waiter"), true, 2). st_next(1, 2).
```

---

## Story #60 — Partial Match (Similarity: 0.3846)

**Story:** Robert ordered a medium-rare steak but received a well-done one. He called the waiter and complained about the mistake. The waiter apologized and took the steak back to the kitchen.

### Predicted
```clingo
restaurant(r). customer("Robert"). food("medium-rare steak"). food("well-done one"). waiter("The waiter"). st_hpd(order("Robert", "medium-rare steak", "The waiter"), true, 0). st_hpd(put_down("The waiter", "well-done one", t), true, 1). st_hpd(complain("Robert", "The waiter"), true, 2).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer("Robert"). food("medium-rare steak"). food("well-done steak"). waiter("the waiter"). story_step(0..3). st_hpd(order("Robert", "medium-rare steak", "the waiter"), true, 0). st_hpd(put_down("the waiter", "well-done steak", t), true, 1). st_hpd(complain("Robert", "the waiter"), true, 2). st_next(1, 2). st_hpd(pick_up("the waiter", "well-done steak", t), true, 3).
```

---

## Story #0 — Partial Match (Similarity: 0.4000)

**Story:** Allie enters the restaurant and claims her reservation. The waiter seats her at her table. She orders fruit salad. The waiter brings her fruit salad. After eating, she asks for the bill.

### Predicted
```clingo
restaurant("the restaurant"). customer("Allie"). food("fruit salad"). waiter("the waiter"). st_hpd(enter("Allie", "the restaurant"), true, 0). st_hpd(lead_to("the waiter", "Allie", t), true, 1). st_hpd(order("Allie", "fruit salad", "the waiter"), true, 2). st_hpd(put_down("the waiter", "fruit salad", t), true, 3). st_hpd(eat("Allie", "fruit salad"), true, 4). st_hpd(request("Allie", b, "the waiter"), true, 5).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer("Allie"). food("fruit salad"). waiter("the waiter"). story_step(0..6). st_hpd(enter("Allie", "the restaurant"), true, 0). st_hpd(lead_to("the waiter", "Allie", t), true, 1). st_hpd(sit("Allie"), true, 2). st_hpd(order("Allie", "fruit salad", "the waiter"), true, 3). st_hpd(put_down("the waiter", "fruit salad", t), true, 4). st_hpd(eat("Allie", "fruit salad"), true, 5). st_hpd(request("Allie", b, "the waiter"), true, 6).
```

---

## Story #16 — Partial Match (Similarity: 0.4000)

**Story:** The waiter took Gavin and Amandine to a booth. They slid onto brown vinyl seats. Gavin glanced over his menu. Amandine didn't need to look to know what she wanted. She ordered egg drop soup with wonton, lobster Cantonese and shrimp, beef and pork fried rice. Gavin ordered the same.

### Predicted
```clingo
restaurant("the restaurant"). customer("Gavin"). customer("Amandine"). waiter("the waiter"). food("egg drop soup with wonton, lobster Cantonese and shrimp, beef and pork fried rice"). st_hpd(lead_to("the waiter", "Gavin", t), true, 0). st_hpd(lead_to("the waiter", "Amandine", t), true, 0). st_hpd(sit("Gavin"), true, 1). st_hpd(sit("Amandine"), true, 1). st_hpd(read_menu("Gavin"), true, 2). st_hpd(read_menu("Amandine"), false, 2). st_hpd(order("Amandine", "egg drop soup with wonton, lobster Cantonese and shrimp, beef and pork fried rice", "the waiter"), true, 3). st_hpd(order("Gavin", "egg drop soup with wonton, lobster Cantonese and shrimp, beef and pork fried rice", "the waiter"), true, 4).
```

### Ground Truth
```clingo
waiter("the waiter"). customer("Gavin"). customer("Amandine"). food(f). member("egg drop soup with wonton", f). member("lobster Cantonese", f). member("shrimp, beef and pork fried rice", f). story_step(0..4). st_hpd(lead_to("the waiter", "Gavin", t), true, 0). st_hpd(lead_to("the waiter", "Amandine", t), true, 0). st_hpd(sit("Gavin"), true, 1). st_hpd(sit("Amandine"), true, 1). st_hpd(read_menu("Gavin"), true, 2). st_hpd(read_menu("Amandine"), false). st_hpd(order("Amandine", f, "the waiter"), true, 3). st_hpd(order("Gavin", f, "the waiter"), true, 4).
```

---

## Story #31 — Partial Match (Similarity: 0.4000)

**Story:** Nicole went to a vegetarian restaurant. She ordered lentil soup. The waitress brought her a miso soup instead. Nicole decided to eat it anyway.

### Predicted
```clingo
restaurant("vegetarian restaurant"). customer("Nicole"). food("lentil soup"). food("miso soup"). waiter("The waitress"). st_hpd(enter("Nicole", "vegetarian restaurant"), true, 0). st_hpd(order("Nicole", "lentil soup", "The waitress"), true, 1). st_hpd(put_down("The waitress", "miso soup", t), true, 2). st_hpd(eat("Nicole", "miso soup"), true, 3).
```

### Ground Truth
```clingo
restaurant(veg_r). customer(nicole). person(owner). food(lentil_soup). food(miso_soup). waiter(waitress). story_step(0..4). st_hpd(enter(nicole, veg_r), true, 0). st_hpd(order(nicole, lentil_soup, waitress), true, 1). st_hpd(put_down(waitress, miso_soup, t), true, 2). stop_activity(nicole, 3). next_st(2, 3). st_hpd(eat(nicole, miso_soup), true, 4).
```

---

## Story #18 — Partial Match (Similarity: 0.4118)

**Story:** Herbie and his father were at a meat restaurant. The waiter brought a sizzling steak that smelled heavenly, and a plate with haddock and creamed spinach. The waiter put Herbie's plate down. Herbieâ€™s father asked the waiter to take the fish away and bring the boy some lamb chops instead.

### Predicted
```clingo
restaurant("meat restaurant"). customer("Herbie"). customer("father"). waiter("the waiter"). food("sizzling steak"). food("plate with haddock and creamed spinach"). food("lamb chops"). st_obs(in("Herbie", "meat restaurant"), true, 0). st_hpd(put_down("the waiter", "sizzling steak", t), true, 1). st_hpd(put_down("the waiter", "plate with haddock and creamed spinach", t), true, 1). st_hpd(request("father", "lamb chops", "the waiter"), true, 2).
```

### Ground Truth
```clingo
restaurant("a meat restaurant"). customer("Herbie"). customer("his father"). food("a sizzling steak"). food("haddock and creamed spinach"). food("lamb chops"). waiter("the waiter"). story_step(0..4). st_obs(in("Herbie", "a meat restaurant"), true, 0). st_obs(in("his father", "a meat restaurant"), true, 0). st_hpd(put_down("the waiter", "a sizzling steak", t), true, 1). st_hpd(put_down("the waiter", "haddock and creamed spinach", t), true, 2). st_hpd(request("his father", pick_up("the waiter", "haddock and creamed spinach", t), "the waiter"), true, 3). st_hpd(order_for("his father", "Herbie", "lamb chops", "the waiter"), true, 4).
```

---

## Story #62 — Partial Match (Similarity: 0.4167)

**Story:** The waiter at the steakhouse brought a rare steak for Wendy, but she had ordered it well-done. She sent it back to the kitchen to be cooked more.

### Predicted
```clingo
restaurant("steakhouse"). customer("Wendy"). food("rare steak"). food("well-done"). waiter("The waiter"). st_hpd(order("Wendy", "well-done", "The waiter"), true, 0). st_hpd(put_down("The waiter", "rare steak", t), true, 1). st_hpd(complain("Wendy", "The waiter"), true, 2).
```

### Ground Truth
```clingo
restaurant("the steakhouse"). customer("Wendy"). food("rare steak"). food("well-done steak"). waiter("the waiter"). story_step(0..2). st_hpd(order("Wendy", "well-done steak", "the waiter"), true, 0). st_hpd(put_down("the waiter", "rare steak", t), true, 1). st_hpd(request("Wendy", pick_up("the waiter", "rare steak", t), "the waiter"), true, 2). st_next(1, 2).
```

---

## Story #22 — Partial Match (Similarity: 0.4211)

**Story:** Andrew was sitting in a restaurant. Sebastian entered the restaurant and sat down opposite Andrew. The waiter brought a bottle of wine. Andrew and Sebastian took a drink. The waiter gave the men a menu.

### Predicted
```clingo
restaurant("restaurant"). customer("Andrew"). customer("Sebastian"). waiter("the waiter"). beverage("bottle of wine"). st_obs(sitting("Andrew"), true, 0). st_hpd(enter("Sebastian", "restaurant"), true, 1). st_hpd(sit("Sebastian"), true, 2). st_hpd(put_down("the waiter", "bottle of wine", t), true, 3). st_hpd(drink("Andrew", "bottle of wine"), true, 4). st_hpd(drink("Sebastian", "bottle of wine"), true, 4). st_hpd(put_down("the waiter", m, t), true, 5).
```

### Ground Truth
```clingo
restaurant("a restaurant"). customer("the men"). person("Andrew"). person("Sebastian"). member("Andrew", "the men"). member("Sebastian", "the men"). beverage(wine). waiter("the waiter"). story_step(0..5). st_obs(in("Andrew", "a restaurant"), true, 0). st_obs(sitting("Andrew"), true, 0). st_hpd(enter("Sebastian", "a restaurant"), true, 1). st_hpd(sit("Sebastian"), true, 2). st_hpd(put_down("the waiter", wine, t), true, 3). st_hpd(drink("the men", wine), true, 4). st_hpd(put_down("the waiter", m, t), true, 5).
```

---

## Story #88 — Partial Match (Similarity: 0.4444)

**Story:** [REDACTED — original ROCStories text; storyid=3a66621b-9dcf-4e32-b085-e4c0a2e89f8f]

### Predicted
```clingo
restaurant("deli"). customer("I"). food("turkey sandwich"). waiter(w). st_obs(in("I", "deli"), true, 0). st_hpd(order("I", "turkey sandwich", w), true, 1). st_hpd(eat("I", "turkey sandwich"), true, 2).
```

### Ground Truth
```clingo
restaurant("little deli"). customer("I"). food("turkey sandwich"). st_obs(hungry("I"), true, 0). st_hpd(order("I", "turkey sandwich", w), true, 1). st_hpd(eat("I", "turkey sandwich"), true, 2).
```

---

## Story #99 — Partial Match (Similarity: 0.4444)

**Story:** [REDACTED — original ROCStories text; storyid=11cd400e-b2b8-4279-9e2e-925de49fee44]

### Predicted
```clingo
restaurant("new restaurant"). customer("The family"). food("tacos"). waiter(w). st_hpd(enter("The family", "new restaurant"), true, 0). st_hpd(eat("The family", "tacos"), true, 1).
```

### Ground Truth
```clingo
restaurant("new restaurant"). customer("The family"). food("different foods"). food("tacos"). st_hpd(enter("The family", "new restaurant"), true, 0). st_hpd(order("The family", "different foods", w), true, 1). st_hpd(eat("The family", "different foods"), true, 2).
```

---

## Story #58 — Partial Match (Similarity: 0.4615)

**Story:** Ben went to the diner for breakfast. He sat at the counter and ordered pancakes with bacon and coffee. The cook prepared his order right in front of him.

### Predicted
```clingo
restaurant("diner"). customer("Ben"). food("pancakes with bacon"). beverage("coffee"). waiter("The cook"). st_hpd(enter("Ben", "diner"), true, 0). st_hpd(sit("Ben"), true, 1). st_hpd(order("Ben", "pancakes with bacon", "The cook"), true, 2). st_hpd(order("Ben", "coffee", "The cook"), true, 2). st_hpd(prepare("The cook", "pancakes with bacon", "The cook"), true, 3).
```

### Ground Truth
```clingo
restaurant("the diner"). customer("Ben"). food("pancakes with bacon"). beverage("coffee"). story_step(0..3). st_hpd(enter("Ben", "the diner"), true, 0). st_hpd(sit("Ben"), true, 1). st_hpd(order("Ben", "pancakes with bacon", w), true, 2). st_hpd(prepare("the cook", "pancakes with bacon", w), true, 3). st_hpd(prepare("the cook", "coffee", "Ben"), true, 3).
```

---

## Story #9 — Partial Match (Similarity: 0.4667)

**Story:** Pete is seated at his table in the restaurant. He has ordered and received his chicken, but is unhappy with how undercooked the chicken is. He complains to the waiter, and asks for a better cooked dish.

### Predicted
```clingo
restaurant("the restaurant"). customer("Pete"). food("chicken"). food("better cooked dish"). waiter("the waiter"). st_obs(sitting("Pete"), true, 0). st_hpd(order("Pete", "chicken", "the waiter"), true, 1). st_hpd(put_down("the waiter", "chicken", t), true, 2). st_hpd(complain("Pete", "the waiter"), true, 3). st_hpd(request("Pete", "better cooked dish", "the waiter"), true, 4).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer("Pete"). food("chicken"). food("undercooked chicken"). food("better cooked chicken"). waiter("the waiter"). story_step(0..4). st_obs(sitting("Pete"), true, 0). st_hpd(order("Pete", "chicken", "the waiter"), true, 1). st_hpd(put_down("the waiter", "undercooked_chicken", t), true, 2). st_hpd(complain("Pete", "the waiter"), true, 3). st_next(2, 3). st_hpd(order("Pete", "better cooked chicken", "the waiter"), true, 4).
```

---

## Story #25 — Partial Match (Similarity: 0.5000)

**Story:** I was the first person to appear at the restaurant. I took my seat at the middle of the table. The head-waiter waited on me himself. I had a capital dinner. Then Uncle Chipperton entered. He paid for the whole dinner.

### Predicted
```clingo
restaurant("the restaurant"). customer("I"). customer("Uncle Chipperton"). waiter("The head-waiter"). food("capital dinner"). st_hpd(enter("I", "the restaurant"), true, 0). st_hpd(sit("I"), true, 1). st_hpd(eat("I", "capital dinner"), true, 2). st_hpd(enter("Uncle Chipperton", "the restaurant"), true, 3). st_hpd(pay("Uncle Chipperton", b), true, 4).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer("I"). waiter("head-waiter") food("capital dinner"). person("Uncle Chipperton"). story_step(0..5). st_hpd(enter("I", "the restaurant"), true, 0). st_hpd(sit("I"), true, 1). st_hpd(put_down("head-waiter", "capital dinner", t), true, 2). st_hpd(eat("I", "capital dinner"), true, 3). st_hpd(enter("Uncle Chipperton", "the restaurant"), true, 4). st_hpd(pay("Uncle Chipperton", b), true, 5).
```

---

## Story #49 — Partial Match (Similarity: 0.5000)

**Story:** The waiter brought the bill to Mark's table. Mark reviewed it and noticed he had been charged for a dessert he didn't order. He called the waiter over to correct the bill.

### Predicted
```clingo
restaurant(r). customer("Mark"). waiter("The waiter"). food("dessert"). st_hpd(put_down("The waiter", b, t), true, 0). st_hpd(read_bill("Mark"), true, 1). st_hpd(order("Mark", "dessert", "The waiter"), false). st_hpd(complain("Mark", "The waiter"), true, 2).
```

### Ground Truth
```clingo
restaurant(r). customer("Mark"). food("dessert"). waiter("the waiter"). st_hpd(put_down("the waiter", b, t), true, 0). st_hpd(pick_up("Mark", b, t), true, 1). st_hpd(request("Mark", "correction", "the waiter"), true, 1).
```

---

## Story #71 — Partial Match (Similarity: 0.5000)

**Story:** Michael entered the bistro and was led to a table by a waitress. He ordered the daily special and a glass of water. The waitress brought his meal promptly. Michael enjoyed his food and asked for the check.

### Predicted
```clingo
restaurant("bistro"). customer("Michael"). food("daily special"). beverage("glass of water"). waiter("waitress"). st_hpd(enter("Michael", "bistro"), true, 0). st_hpd(lead_to("waitress", "Michael", t), true, 1). st_hpd(order("Michael", "daily special", "waitress"), true, 2). st_hpd(order("Michael", "glass of water", "waitress"), true, 2). st_hpd(put_down("waitress", "daily special", t), true, 3). st_hpd(put_down("waitress", "glass of water", t), true, 3). st_hpd(eat("Michael", "daily special"), true, 4). st_hpd(request("Michael", b, "waitress"), true, 5).
```

### Ground Truth
```clingo
restaurant("the bistro"). customer("Michael"). food("daily special"). beverage("water"). waiter("the waitress"). st_hpd(enter("Michael", "the bistro"), true, 0). st_hpd(lead_to("the host", "Michael", t), true, 1). st_hpd(order("Michael", "daily special", "the waitress"), true, 2). st_hpd(order("Michael", "water", "the waitress"), true, 2). st_hpd(put_down("the waitress", "daily special", t), true, 3). st_hpd(put_down("the waitress", "water", t), true, 3). st_hpd(eat("Michael", "daily special"), true, 4). st_hpd(drink("Michael", "water"), true, 4). st_hpd(request("Michael", b, "the waitress"), true, 5).
```

---

## Story #8 — Partial Match (Similarity: 0.5455)

**Story:** Derek ordered a vegetable soup. The waiter brought out the vegetable soup, but Derek was unsatisfied with the lack of vegetables in it. As an apology, the waiter decided not to charge Derek for the soup.

### Predicted
```clingo
restaurant(r). customer("Derek"). food("vegetable soup"). waiter("the waiter"). st_hpd(order("Derek", "vegetable soup", "the waiter"), true, 0). st_hpd(put_down("the waiter", "vegetable soup", t), true, 1). st_hpd(complain("Derek", "the waiter"), true, 2). st_hpd(cancel_bill("the waiter"), true, 3).
```

### Ground Truth
```clingo
restaurant("restaurant"). customer("Derek"). food("vegetable soup"). waiter("the waiter"). story_step(0..3). st_hpd(order("Derek", "vegetable soup", "the waiter"), true, 0). st_hpd(put_down("the waiter", "vegetable soup", t), true, 1). st_hpd(complain("Derek", "the waiter"), true, 2). st_next(1, 2). st_hpd(pay("derek", b), false, 3).
```

---

## Story #30 — Partial Match (Similarity: 0.5455)

**Story:** Nicole went to a vegetarian restaurant. She ordered lentil soup. The waitress brought her a miso soup instead.

### Predicted
```clingo
restaurant("vegetarian restaurant"). customer("Nicole"). food("lentil soup"). food("miso soup"). waiter("The waitress"). st_hpd(enter("Nicole", "vegetarian restaurant"), true, 0). st_hpd(order("Nicole", "lentil soup", "The waitress"), true, 1). st_hpd(put_down("The waitress", "miso soup", t), true, 2).
```

### Ground Truth
```clingo
restaurant(veg_r). customer(nicole). person(owner). food(lentil_soup). food(miso_soup). waiter(waitress). story_step(0..2). st_hpd(enter(nicole, veg_r), true, 0). st_hpd(order(nicole, lentil_soup, waitress), true, 1). st_hpd(put_down(waitress, miso_soup, t), true, 2).
```

---

## Story #42 — Partial Match (Similarity: 0.5556)

**Story:** David and his date, Sarah, went to a fancy restaurant. David ordered for both of them, choosing the duck confit. The waiter served the meal and poured them some wine. They enjoyed their dinner.

### Predicted
```clingo
restaurant("fancy restaurant"). customer("David"). customer("Sarah"). member("David", they). member("Sarah", they). food("duck confit"). beverage("wine"). waiter("The waiter"). st_hpd(enter(they, "fancy restaurant"), true, 0). st_hpd(order("David", "duck confit", "The waiter"), true, 1). st_hpd(order_for("David", "Sarah", "duck confit", "The waiter"), true, 1). st_hpd(put_down("The waiter", "duck confit", t), true, 2). st_hpd(put_down("The waiter", "wine", t), true, 2). st_hpd(eat(they, "duck confit"), true, 3).
```

### Ground Truth
```clingo
restaurant("fancy restaurant"). customer(they). person("David"). person("Sarah"). member("David", they). member("Sarah", they). food("duck confit"). beverage("wine"). waiter("the waiter"). story_step(0..3). st_hpd(order_for("David", they, "duck confit", "the waiter"), true, 0). st_hpd(put_down("the waiter", "duck confit", t), true, 1). st_hpd(put_down("the waiter", "wine", t), true, 2). st_hpd(eat(they, "duck confit"), true, 3). st_hpd(drink(they, "wine"), true, 3).
```

---

## Story #26 — Partial Match (Similarity: 0.6364)

**Story:** Nicole went to a vegetarian restaurant. She ordered lentil soup. The waitress set the soup in the middle of the table. Nicole enjoyed the soup. She left the restaurant.

### Predicted
```clingo
restaurant("vegetarian restaurant"). customer("Nicole"). food("lentil soup"). waiter("The waitress"). st_hpd(enter("Nicole", "vegetarian restaurant"), true, 0). st_hpd(order("Nicole", "lentil soup", "The waitress"), true, 1). st_hpd(put_down("The waitress", "lentil soup", t), true, 2). st_hpd(eat("Nicole", "lentil soup"), true, 3). st_hpd(leave("Nicole"), true, 4).
```

### Ground Truth
```clingo
restaurant(veg_r). customer(nicole). food(lentil_soup). waiter(waitress). story_step(0..4). st_hpd(enter(nicole, veg_r), true, 0). st_hpd(order(nicole, lentil_soup, waitress), true, 1). st_hpd(put_down(waitress, lentil_soup, t), true, 2). st_hpd(eat(nicole, lentil_soup), true, 3). st_hpd(leave(nicole), true, 4).
```

---

## Story #10 — Partial Match (Similarity: 0.6667)

**Story:** Jim is seated at his table in the restaurant. He orders an appetizer. After waiting for 20 minutes and not receiving his food, he decides to leave the restaurant.

### Predicted
```clingo
restaurant("the restaurant"). customer("Jim"). food("appetizer"). waiter(w). st_obs(sitting("Jim"), true, 0). st_hpd(order("Jim", "appetizer", w), true, 1). st_obs(served("Jim"), false, 2). st_hpd(leave("Jim"), true, 3).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer("Jim"). food("appetizer"). story_step(0..3). st_obs(sitting("Jim"), true, 0). st_hpd(order("Jim", "appetizer", w), true, 1). st_obs(served("Pete"), false, 2). st_hpd(leave("Jim"), true, 3).
```

---

## Story #11 — Partial Match (Similarity: 0.6667)

**Story:** Jake is seated at his table in the restaurant. He orders a medium-rare steak. The waiter brings out his order but it is too rare.

### Predicted
```clingo
restaurant("the restaurant"). customer("Jake"). food("medium-rare steak"). waiter("the waiter"). st_obs(sitting("Jake"), true, 0). st_hpd(order("Jake", "medium-rare steak", "the waiter"), true, 1). st_hpd(put_down("the waiter", "medium-rare steak", t), true, 2).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer("Jake"). food("medium-rare steak"). food("too rare steak"). waiter("the waiter"). story_step(0..2). st_obs(sitting("Jake"), true, 0). st_hpd(order("Jake", "medium-rare steak", "the waiter"), true, 1). st_hpd(put_down("the waiter", "too rare steak", t), true, 2).
```

---

## Story #51 — Partial Match (Similarity: 0.6667)

**Story:** Steve and his son entered a pizzeria. The waiter took them to a table by the window. They ordered a large pepperoni pizza to share. After eating, Steve paid the bill.

### Predicted
```clingo
restaurant("pizzeria"). customer("Steve"). customer("son"). member("Steve", they). member("son", they). food("large pepperoni pizza"). waiter("The waiter"). st_hpd(enter(they, "pizzeria"), true, 0). st_hpd(lead_to("The waiter", they, t), true, 1). st_hpd(order(they, "large pepperoni pizza", "The waiter"), true, 2). st_hpd(eat(they, "large pepperoni pizza"), true, 3). st_hpd(pay("Steve", b), true, 4).
```

### Ground Truth
```clingo
restaurant("pizzeria"). customer(they). person("Steve"). person("his son"). member("Steve", they). member("his son", they). food("large pepperoni pizza"). waiter("the waiter"). story_step(0..4). st_hpd(enter(they, "pizzeria"), true, 0). st_hpd(lead_to("the waiter", they, t), true, 1). st_hpd(order(they, "large pepperoni pizza", "the waiter"), true, 2). st_hpd(eat(they, "large pepperoni pizza"), true, 3). st_hpd(pay("Steve", b), true, 4).
```

---

## Story #56 — Partial Match (Similarity: 0.6667)

**Story:** Anna visited the vegan restaurant downtown. She ordered the quinoa bowl and a green smoothie. The food was fresh and delicious. She left a generous tip for the excellent service.

### Predicted
```clingo
restaurant("vegan restaurant"). customer("Anna"). food("quinoa bowl"). beverage("green smoothie"). waiter(w). st_hpd(enter("Anna", "vegan restaurant"), true, 0). st_hpd(order("Anna", "quinoa bowl", w), true, 1). st_hpd(order("Anna", "green smoothie", w), true, 1). st_hpd(pay("Anna", tip), true, 2).
```

### Ground Truth
```clingo
restaurant("vegan restaurant"). customer("Anna"). food("quinoa bowl"). beverage("green smoothie"). waiter(w). story_step(0..4). st_hpd(enter("Anna", "vegan restaurant"), true, 0). st_hpd(order("Anna", "quinoa bowl", w), true, 1). st_hpd(order("Anna", "green smoothie", w), true, 1). st_hpd(eat("Anna", "quinoa bowl"), true, 3). st_hpd(drink("Anna", "green smoothie"), true, 3). st_hpd(pay("Anna", tip), true, 4).
```

---

## Story #13 — Partial Match (Similarity: 0.6923)

**Story:** Judy looked at the menu. She and her two kids, Alex and Zoe, were seated in a booth in a local restaurant. They ordered fish and chips.

### Predicted
```clingo
restaurant("local restaurant"). customer("Judy"). customer("Alex"). customer("Zoe"). member("Judy", they). member("Alex", they). member("Zoe", they). food("fish and chips"). st_obs(sitting(they), true, 0). st_hpd(read_menu("Judy"), true, 1). st_hpd(order(they, "fish and chips", w), true, 2).
```

### Ground Truth
```clingo
restaurant("a local restaurant"). person("Judy"). person("Alex"). person("Zoe"). customer("they"). member("Judy", "they"). member("Alex", "they"). member("Zoe", "they"). food("fish and chips"). story_step(0..1). st_obs(sitting("they"), true, 0). st_hpd(order("they", "fish and chips", w), true, 1).
```

---

## Story #95 — Partial Match (Similarity: 0.6923)

**Story:** [REDACTED — original ROCStories text; storyid=cd9a0a7b-ef8f-42c0-86ac-fe80542cebd3]

### Predicted
```clingo
restaurant("restaurant"). customer("homeless man"). waiter("Austin"). waiter("The wait staff"). food("spare food"). food("full meal"). st_hpd(enter("homeless man", "restaurant"), true, 0). st_hpd(request("homeless man", "spare food", "Austin"), true, 1). st_hpd(lead_to("Austin", "homeless man", t), true, 2). st_hpd(put_down("The wait staff", "full meal", t), true, 3). st_hpd(pay("homeless man", b), false).
```

### Ground Truth
```clingo
restaurant("a restaurant"). customer("a homeless man"). waiter("wait staff"). person("Austin"). food("spare food"). food("full meal").  st_hpd(enter("a homeless man", "a restaurant"), true, 0). st_hpd(request("a homeless man", "spare food", "Austin"), true, 1). st_hpd(sit("a homeless man"), true, 2). st_hpd(put_down("wait staff", "full meal", t), true, 3). st_hpd(pay("a homeless man", b), false).
```

---

## Story #83 — Partial Match (Similarity: 0.7143)

**Story:** [REDACTED — original ROCStories text; storyid=9c2ccb82-003d-4253-9f19-65b157b9993f]

### Predicted
```clingo
restaurant("diner"). customer("The couple"). waiter("The waitress"). st_hpd(sit("The couple"), true, 0). st_hpd(stand_up("The couple"), true, 1). st_hpd(order("The couple", f, "The waitress"), true, 2).
```

### Ground Truth
```clingo
restaurant("diner"). customer("the couple"). waiter("the waitress"). st_hpd(sit("the couple"), true, 0). st_hpd(greet("the waitress", "the couple"), false). st_hpd(stand_up("the couple"), true, 1).
```

---

## Story #90 — Partial Match (Similarity: 0.7273)

**Story:** [REDACTED — original ROCStories text; storyid=c4078b0f-e1c3-4c75-a05a-a52c9481fc2a]

### Predicted
```clingo
restaurant("restaurant"). customer("My family"). customer("I"). member("I", "My family"). food("five course meal"). food("bread"). food("salmon and asparagus"). waiter(w). st_hpd(enter("My family", "restaurant"), true, 0). st_hpd(eat("My family", "bread"), true, 1). st_hpd(eat("I", "salmon and asparagus"), true, 1).
```

### Ground Truth
```clingo
restaurant("a restaurant"). customer("My family"). customer("I"). food("bread"). food("salmon and asparagus"). st_hpd(enter("My family", "a restaurant"), true, 0). st_hpd(eat("My family", "bread"), true, 1). st_hpd(eat("I", "salmon and asparagus"), true, 1).
```

---

## Story #54 — Partial Match (Similarity: 0.7692)

**Story:** Sarah visited the cafe for lunch. She sat at a table by the window and ordered a chicken sandwich and coffee. The waitress brought her order. Sarah ate quickly as she was in a hurry.

### Predicted
```clingo
restaurant("cafe"). customer("Sarah"). food("chicken sandwich"). beverage("coffee"). waiter("The waitress"). st_hpd(enter("Sarah", "cafe"), true, 0). st_hpd(sit("Sarah"), true, 1). st_hpd(order("Sarah", "chicken sandwich", "The waitress"), true, 2). st_hpd(order("Sarah", "coffee", "The waitress"), true, 2). st_hpd(put_down("The waitress", "chicken sandwich", t), true, 3). st_hpd(put_down("The waitress", "coffee", t), true, 3). st_hpd(eat("Sarah", "chicken sandwich"), true, 4).
```

### Ground Truth
```clingo
restaurant("the cafe"). customer("Sarah"). food("chicken sandwich"). beverage("coffee"). waiter("the waitress"). story_step(0..4). st_hpd(enter("Sarah", "the cafe"), true, 0). st_hpd(sit("Sarah"), true, 1). st_hpd(order("Sarah", "chicken sandwich", "the waitress"), true, 2). st_hpd(put_down("the waitress", "chicken sandwich", t), true, 3). st_hpd(eat("Sarah", "chicken sandwich"), true, 4). st_hpd(drink("Sarah", "coffee"), true, 4).
```

---

## Story #68 — Partial Match (Similarity: 0.8462)

**Story:** Frank sat down at his usual table in the local diner. The waitress brought him a black coffee. Frank looked at the menu and then ordered pancakes. He ate them, left cash on the table for the bill, and left.

### Predicted
```clingo
restaurant("local diner"). customer("Frank"). beverage("black coffee"). food("pancakes"). waiter("The waitress"). st_hpd(sit("Frank"), true, 0). st_hpd(put_down("The waitress", "black coffee", t), true, 1). st_hpd(read_menu("Frank"), true, 2). st_hpd(order("Frank", "pancakes", "The waitress"), true, 3). st_hpd(eat("Frank", "pancakes"), true, 4). st_hpd(pay("Frank", b), true, 5). st_hpd(leave("Frank"), true, 6).
```

### Ground Truth
```clingo
restaurant("local diner"). customer("Frank"). beverage("black coffee"). food("pancakes"). waiter("the waitress"). story_step(0..6). st_obs(sitting("Frank"), true, 0). st_hpd(put_down("the waitress", "black coffee", t), true, 1). st_hpd(read_menu("Frank"), true, 2). st_hpd(order("Frank", "pancakes", "the waitress"), true, 3). st_hpd(eat("Frank", "pancakes"), true, 4). st_hpd(pay("Frank", b), true, 5). st_hpd(leave("Frank"), true, 6).
```

---

## Story #86 — Partial Match (Similarity: 0.8462)

**Story:** [REDACTED — original ROCStories text; storyid=541efb12-b331-4525-afe1-5422ff33a1ca]

### Predicted
```clingo
restaurant("diner"). customer("Samuel"). customer("John"). food("hamburger without onions"). food("hotdog"). waiter("The waiter"). st_obs(in("Samuel", "diner"), true, 0). st_hpd(order("Samuel", "hamburger without onions", "The waiter"), true, 1). st_hpd(put_down("The waiter", "hotdog", t), true, 2). st_hpd(complain("Samuel", "The waiter"), true, 3). st_hpd(put_down("The waiter", "hamburger without onions", t), true, 4).
```

### Ground Truth
```clingo
restaurant("diner"). customer("Samuel"). customer("John"). food("hamburger without onions"). food("hotdog"). waiter("the waiter"). st_obs(in("Samuel", "diner"), true, 0). st_obs(in("John", "diner"), true, 0). st_hpd(order("Samuel", "hamburger without onions", "the waiter"), true, 1). st_hpd(put_down("the waiter", "hotdog", t), true, 2). st_hpd(complain("Samuel", "the waiter"), true, 3). st_next(2,3). st_hpd(put_down("the waiter", "hamburger without onions", t), true, 4).
```

---

## Story #46 — Partial Match (Similarity: 0.8750)

**Story:** Rita finished her salad. She requested the bill from the waiter. The waiter brought the bill, and Rita paid with her credit card.

### Predicted
```clingo
customer("Rita"). waiter("The waiter"). food("salad"). st_hpd(eat("Rita", "salad"), true, 0). st_hpd(request("Rita", b, "The waiter"), true, 1). st_hpd(put_down("The waiter", b, t), true, 2). st_hpd(pay("Rita", b), true, 3).
```

### Ground Truth
```clingo
restaurant(r). customer("Rita"). food("salad"). waiter("the waiter"). story_step(0..3). st_hpd(eat("Rita", "salad"), true, 0). st_hpd(request("Rita", b, "the waiter"), true, 1). st_hpd(put_down("the waiter", b, t), true, 2). st_hpd(pay("Rita", b), true, 3).
```

---

## Story #69 — Partial Match (Similarity: 0.9091)

**Story:** A group of coworkers went to a sandwich shop for lunch. The waiter seated them at a long table, and took their orders. The waiter brought out all the sandwiches. They ate, paid their separate bills, and returned to work.

### Predicted
```clingo
restaurant("sandwich shop"). customer("group of coworkers"). food("sandwiches"). waiter("The waiter"). st_hpd(enter("group of coworkers", "sandwich shop"), true, 0). st_hpd(lead_to("The waiter", "group of coworkers", t), true, 1). st_hpd(order("group of coworkers", "sandwiches", "The waiter"), true, 2). st_hpd(put_down("The waiter", "sandwiches", t), true, 3). st_hpd(eat("group of coworkers", "sandwiches"), true, 4). st_hpd(pay("group of coworkers", b), true, 5).
```

### Ground Truth
```clingo
restaurant("sandwich shop"). customer("group of coworkers"). food("sandwiches"). waiter("the waiter"). st_hpd(enter("group of coworkers", "sandwich shop"), true, 0). st_hpd(lead_to("the waiter", "group of coworkers", t), true, 1). st_hpd(order("group of coworkers", "sandwiches", "the waiter"), true, 2). st_hpd(put_down("the waiter", "sandwiches", t), true, 3). st_hpd(eat("group of coworkers", "sandwiches"), true, 4). st_hpd(pay("group of coworkers", b), true, 5). st_hpd(leave("group of coworkers"), true, 6).
```

---

## Story #70 — Partial Match (Similarity: 0.9167)

**Story:** The Jackson family went to a pizzeria on Friday night. The waiter led them to a booth. They ordered a large pepperoni pizza and a pitcher of soda. The waiter brought their order to the table. They all loved the pizza.

### Predicted
```clingo
restaurant("pizzeria"). customer("Jackson family"). food("large pepperoni pizza"). beverage("pitcher of soda"). waiter("The waiter"). st_hpd(enter("Jackson family", "pizzeria"), true, 0). st_hpd(lead_to("The waiter", "Jackson family", t), true, 1). st_hpd(order("Jackson family", "large pepperoni pizza", "The waiter"), true, 2). st_hpd(order("Jackson family", "pitcher of soda", "The waiter"), true, 2). st_hpd(put_down("The waiter", "large pepperoni pizza", t), true, 3). st_hpd(put_down("The waiter", "pitcher of soda", t), true, 3).
```

### Ground Truth
```clingo
restaurant("pizzeria"). customer("The Jackson family"). food("large pepperoni pizza"). beverage("pitcher of soda"). waiter("the waiter"). st_hpd(enter("The Jackson family", "pizzeria"), true, 0). st_hpd(lead_to("the waiter", "The Jackson family", t), true, 1). st_hpd(order("The Jackson family", "large pepperoni pizza", "the waiter"), true, 2). st_hpd(order("The Jackson family", "pitcher of soda", "the waiter"), true, 2). st_hpd(put_down("the waiter", "large pepperoni pizza", t), true, 3). st_hpd(put_down("the waiter", "pitcher of soda", t), true, 3). st_hpd(eat("The Jackson family", "large pepperoni pizza"), true, 4).
```

---

## Story #72 — Partial Match (Similarity: 0.9167)

**Story:** Susan visited the pancake house for breakfast. She ordered blueberry pancakes and orange juice. The server brought her order quickly. Susan ate her breakfast and paid with her credit card.

### Predicted
```clingo
restaurant("pancake house"). customer("Susan"). food("blueberry pancakes"). beverage("orange juice"). waiter("The server"). st_hpd(enter("Susan", "pancake house"), true, 0). st_hpd(order("Susan", "blueberry pancakes", "The server"), true, 1). st_hpd(order("Susan", "orange juice", "The server"), true, 1). st_hpd(put_down("The server", "blueberry pancakes", t), true, 2). st_hpd(put_down("The server", "orange juice", t), true, 2). st_hpd(eat("Susan", "blueberry pancakes"), true, 3). st_hpd(pay("Susan", b), true, 4).
```

### Ground Truth
```clingo
restaurant("the pancake house"). customer("Susan"). food("blueberry pancakes"). beverage("orange juice"). waiter("the server"). st_hpd(enter("Susan", "the pancake house"), true, 0). st_hpd(order("Susan", "blueberry pancakes", "the server"), true, 1). st_hpd(order("Susan", "orange juice", "the server"), true, 1). st_hpd(put_down("the server", "blueberry pancakes", t), true, 2). st_hpd(eat("Susan", "blueberry pancakes"), true, 3). st_hpd(pay("Susan", b), true, 4).
```

---
