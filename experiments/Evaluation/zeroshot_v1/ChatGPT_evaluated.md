# ChatGPT_evaluated

## Summary

- Total common: 100
- Exact matches: 0
- Partial matches: 100
- Accuracy: 0.0

---

## Story #24 — Partial Match (Similarity: 0.0400)

**Story:** Jasper invited Frank to a restaurant. Jasper ordered roast beef and coffee. Their conversation was interrupted by the arrival of the coffee and roast beef, which both he and his new friend attacked with vigor. Jasper wanted to invite Frank, but he had forgotten his wallet at home. Frank paid for both.

### Predicted
```clingo
person("Jasper") person("Frank") customer("Jasper") customer("Frank") restaurant(r) waiter(w) food("roast beef") beverage("coffee") st_hpd(order("Jasper", "roast beef", w), true, 0) st_hpd(order("Jasper", "coffee", w), true, 0) st_obs(served("Jasper"), true, 1) st_obs(served("Frank"), true, 1) st_hpd(pay("Frank", b), true, 2) st_hpd(pay("Jasper", b), false)
```

### Ground Truth
```clingo
restaurant("a restaurant"). customer(they). member("Jasper", they). member("Frank", they). food(f). member("roast beef", f). member(coffee, f). waiter(w). story_step(0..4). st_hpd(enter(they, "a restaurant"), true, 0). st_hpd(order_for("Jasper", they, f, w), true, 1). st_hpd(put_down(w, f, t), true, 2). st_hpd(eat(they, f), true, 3). st_hpd(pay("Jasper", b), false, 4). st_hpd(pay("Frank", b), true, 4).
```

---

## Story #18 — Partial Match (Similarity: 0.0714)

**Story:** Herbie and his father were at a meat restaurant. The waiter brought a sizzling steak that smelled heavenly, and a plate with haddock and creamed spinach. The waiter put Herbie's plate down. Herbieâ€™s father asked the waiter to take the fish away and bring the boy some lamb chops instead.

### Predicted
```clingo
person("Herbie"). customer("Herbie"). person("Herbie's father"). customer("Herbie's father"). restaurant(r). waiter(w). food("steak"). food("haddock"). food("creamed spinach"). food("lamb chops"). st_obs(in("Herbie", r), true, 0). st_obs(in("Herbie's father", r), true, 0). st_hpd(put_down(w, "steak", t), true, 1). st_hpd(put_down(w, f, t), true, 1). member("haddock", f). member("creamed spinach", f). st_obs(served("Herbie"), true, 2). st_hpd(request("Herbie's father", "take the fish away", w), true, 3). st_hpd(order_for("Herbie's father", "Herbie", "lamb chops", w), true, 3).
```

### Ground Truth
```clingo
restaurant("a meat restaurant"). customer("Herbie"). customer("his father"). food("a sizzling steak"). food("haddock and creamed spinach"). food("lamb chops"). waiter("the waiter"). story_step(0..4). st_obs(in("Herbie", "a meat restaurant"), true, 0). st_obs(in("his father", "a meat restaurant"), true, 0). st_hpd(put_down("the waiter", "a sizzling steak", t), true, 1). st_hpd(put_down("the waiter", "haddock and creamed spinach", t), true, 2). st_hpd(request("his father", pick_up("the waiter", "haddock and creamed spinach", t), "the waiter"), true, 3). st_hpd(order_for("his father", "Herbie", "lamb chops", "the waiter"), true, 4).
```

---

## Story #67 — Partial Match (Similarity: 0.0732)

**Story:** Maria and Leo entered a quiet Italian restaurant. The waiter seated them at a corner table. They ordered a bottle of red wine. After the waiter brought the wine, they ordered two pasta dishes. They enjoyed their meal, paid the bill, and left.

### Predicted
```clingo
restaurant("quiet Italian restaurant"). waiter(w). person("Maria"). customer("Maria"). person("Leo"). customer("Leo"). customer("group"). member("Maria", "group"). member("Leo", "group"). beverage("bottle of red wine"). food("pasta dish 1"). food("pasta dish 2"). st_hpd(enter("Maria", "quiet Italian restaurant"), true, 0). st_hpd(enter("Leo", "quiet Italian restaurant"), true, 0). st_hpd(lead_to(w, "Maria", t), true, 1). st_hpd(lead_to(w, "Leo", t), true, 1). st_hpd(sit("Maria"), true, 2). st_hpd(sit("Leo"), true, 2). st_hpd(order("group", "bottle of red wine", w), true, 3). st_obs(at_l("bottle of red wine", t), true, 4). st_hpd(order("group", f, w), true, 5). member("pasta dish 1", f). member("pasta dish 2", f). st_hpd(drink("group", "bottle of red wine"), true, 6). st_hpd(eat("group", f), true, 7). st_hpd(pay("group", b), true, 8). st_hpd(leave("Maria"), true, 9). st_hpd(leave("Leo"), true, 9).
```

### Ground Truth
```clingo
restaurant("quiet Italian restaurant"). customer(they). person("Maria"). person("Leo"). member("Maria", they). member("Leo", they). beverage("red wine"). food("pasta dishes"). waiter("the waiter"). story_step(0..7). st_hpd(enter(they, "quiet Italian restaurant"), true, 0). st_hpd(lead_to("the waiter", they, t), true, 1). st_hpd(order(they, "red wine", "the waiter"), true, 2). st_hpd(put_down("the waiter", "red wine", t), true, 3). st_hpd(order(they, "pasta dishes", "the waiter"), true, 4). st_hpd(eat(they, "pasta dishes"), true, 5). st_hpd(drink(they, "red wine"), true, 5). st_hpd(pay(they, b), true, 6). st_hpd(leave(they), true, 7).
```

---

## Story #21 — Partial Match (Similarity: 0.0800)

**Story:** The waiter brought the wine to their table. Then, Emanuel studied the menu. He ordered the gypsy shashlik for Ingrid and himself. After the waiter left, they drank the wine. The waiter brought the shashlik to their table.

### Predicted
```clingo
person("Emanuel") person("Ingrid") customer("Emanuel") customer("Ingrid") waiter(w) beverage("wine") food("gypsy shashlik") member("Emanuel", "they") member("Ingrid", "they") st_obs(served("Emanuel"), true, 0) st_obs(served("Ingrid"), true, 0) st_hpd(read_menu("Emanuel"), true, 1) st_hpd(order_for("Emanuel", "Ingrid", "gypsy shashlik", w), true, 2) st_hpd(order_for("Emanuel", "Emanuel", "gypsy shashlik", w), true, 2) st_hpd(drink("Emanuel", "wine"), true, 3) st_hpd(drink("Ingrid", "wine"), true, 3)
```

### Ground Truth
```clingo
restaurant(r). customer(they). member("Emanuel"). member("Ingrid"). beverage(wine). food("gypsy shashlik"). waiter("the waiter"). story_step(0..5). st_hpd(put_down("the waiter", wine, t), true, 0). st_hpd(pick_up("Emanuel", m, t), true, 1). st_hpd(order_for("Emanuel", they, "gypsy shashlik", "the waiter"), true, 2). st_hpd(move("the waiter", t, kitchen), true, 3). st_hpd(drink(they, wine), true, 4). st_hpd(put_down("the waiter", "gypsy shashlik", t), true, 5).
```

---

## Story #64 — Partial Match (Similarity: 0.0800)

**Story:** Penny booked a table for two. She and her friend arrived at the restaurant and were seated immediately. They perused the menu, ordered their food, and had a lovely meal.

### Predicted
```clingo
person("Penny"). customer("Penny"). person("her friend"). customer("her friend"). waiter(w). st_hpd(enter("Penny", r), true, 0). st_hpd(enter("her friend", r), true, 0). st_hpd(lead_to(w, "Penny", t), true, 1). st_hpd(lead_to(w, "her friend", t), true, 1). st_hpd(sit("Penny"), true, 2). st_hpd(sit("her friend"), true, 2). st_hpd(read_menu("Penny"), true, 3). st_hpd(read_menu("her friend"), true, 3). st_hpd(order("Penny", f, w), true, 4). st_hpd(order("her friend", f, w), true, 4). st_hpd(eat("Penny", f), true, 5). st_hpd(eat("her friend", f), true, 5).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer(they). person("Penny"). person("her friend"). member("Penny", they). member("her friend", they). food("food"). story_step(0..5). st_hpd(enter(they, "the restaurant"), true, 0). st_hpd(sit(they), true, 1). st_hpd(read_menu(they), true, 3). st_hpd(order(they, "food", w), true, 4). st_hpd(eat(they, "food"), true, 5).
```

---

## Story #19 — Partial Match (Similarity: 0.0811)

**Story:** Brand sat in a chair. He picked up the menu and ordered a whiskey with Pepsi, but no ice. Pyrogies and sausage cooked in sauerkraut, he told the waiter. The waiter brought Brand his drink. Then, the waiter placed the food on the table. Brand asked the waiter to bring him a large bowl of borscht when he was done with the pyrogies and sausage. The waiter went back into the kitchen. Brand ate the pyrogies and then the sausage and sauerkraut. Then, the waiter brought out Brand's bowl of soup.

### Predicted
```clingo
person("Brand"). customer("Brand"). waiter(w). beverage("whiskey with Pepsi"). food("pyrogies"). food("sausage"). food("sauerkraut"). food("borscht"). st_obs(sitting("Brand"), true, 0). st_hpd(pick_up("Brand", "menu", t), true, 1). st_hpd(order("Brand", "whiskey with Pepsi", w), true, 2). st_hpd(order("Brand", f, w), true, 3). member("pyrogies", f). member("sausage", f). member("sauerkraut", f). st_hpd(put_down(w, "whiskey with Pepsi", t), true, 4). st_hpd(put_down(w, f, t), true, 5). st_hpd(order("Brand", "borscht", w), true, 6). st_hpd(move(w, t, "kitchen"), true, 7). st_hpd(eat("Brand", "pyrogies"), true, 8). st_hpd(eat("Brand", "sausage"), true, 9). st_hpd(eat("Brand", "sauerkraut"), true, 10). st_hpd(put_down(w, "borscht", t), true, 11).
```

### Ground Truth
```clingo
restaurant(r). customer("Brand"). beverage("whiskey with Pepsi, no ice"). food(f). member(pyrogies, f). member("sausage in sauerkraut", f). food(borscht). waiter("the waiter"). story_step(0..9). st_hpd(sit("Brand"), true, 0). st_hpd(pick_up("Brand", m, t), true, 1). st_hpd(order("Brand", "whiskey with Pepsi, no ice", "the waiter"), true, 2). st_hpd(order("Brand", f, "the waiter"), true, 3). st_hpd(put_down("the waiter", "whiskey with Pepsi, no ice"), t), true, 4). st_hpd(put_down("the waiter", f, t), true, 5). st_hpd(order("Brand", borscht, "the waiter"), true, 6). st_hpd(move("the waiter", t, kitchen), true, 7). st_hpd(eat("Brand", f), true, 8). st_hpd(put_down("the waiter", borscht, t), true, 9).
```

---

## Story #45 — Partial Match (Similarity: 0.0833)

**Story:** The restaurant was very busy. A group of friends was seated, but no waiter came to take their order. After waiting for twenty minutes, they decided to leave and go somewhere else.

### Predicted
```clingo
restaurant(r). waiter(w). customer("friends"). person("friends"). st_obs(at_l("friends", t), true, 0). st_obs(sitting("friends"), true, 0). st_hpd(order("friends"), false). st_hpd(leave("friends"), true, 1).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer("group of friends"). waiter(w). story_step(0..2). st_obs(sitting("group of friends"), true, 0). st_hpd(served("group of friends"), false). st_hpd(leave("group of friends"), true, 1).
```

---

## Story #17 — Partial Match (Similarity: 0.0909)

**Story:** The waiter brought his dinner. He was eating something spotted with eggs and livers. He finished but the waiter wouldn't come total the bill.

### Predicted
```clingo
person("the customer"). customer("the customer"). waiter(w). food("something spotted with eggs and livers"). st_hpd(put_down(w, "something spotted with eggs and livers", t), true, 0). st_hpd(eat("the customer", "something spotted with eggs and livers"), true, 1). st_obs(bill_generated("the customer", b), false, 2).
```

### Ground Truth
```clingo
customer("he"). food("something spotted with eggs and livers"). waiter("the waiter"). story_step(0..1). st_hpd(put_down("the waiter", "something spotted with eggs and livers", t), true, 0). st_hpd(eat("he", "something spotted with eggs and livers"), true, 1). st_hpd(put_down("the waiter", b, t), false).
```

---

## Story #82 — Partial Match (Similarity: 0.1111)

**Story:** [REDACTED — original ROCStories text; storyid=2cf524c3-5e49-4ba9-9590-f84429fbdc01]

### Predicted
```clingo
person("Elmer") person("Emma") restaurant("the new restaurant in town") waiter(w) food("burger") beverage("milkshake") food("fries") member("Elmer", g1) member("Emma", g1) st_hpd(enter("Elmer", "the new restaurant in town"), true, 0) st_hpd(enter("Emma", "the new restaurant in town"), true, 0) st_hpd(order("Elmer", "burger", w), true, 1) st_hpd(order("Emma", "burger", w), true, 1) st_hpd(order("Elmer", "milkshake", w), true, 2) st_hpd(order("Emma", "milkshake", w), true, 2) st_hpd(order("Elmer", "fries", w), true, 3) member("fries", g1)
```

### Ground Truth
```clingo
restaurant("new restaurant"). customer("the couple"). person("Elmer"). person("Emma"). member("Elmer", "the couple"). member("Emma", "the couple"). food("burgers"). food("fries"). beverage("milkshakes"). st_hpd(enter("the couple", "new restaurant"), true, 0). st_hpd(order("the couple", "burgers", w), true, 1). st_hpd(order("the couple", "milkshakes", w), true, 1). st_hpd(order("Elmer", "fries", w), true, 2).
```

---

## Story #94 — Partial Match (Similarity: 0.1111)

**Story:** [REDACTED — original ROCStories text; storyid=63dfd3a4-930a-4a27-8ed9-60304b6c32f3]

### Predicted
```clingo
customer("the couple"). restaurant("the new sushi place in town"). food("food"). st_hpd(enter("the couple", "the new sushi place in town"), true, 0). st_hpd(eat("the couple", "food"), true, 1).
```

### Ground Truth
```clingo
restaurant("new sushi place"). customer("The couple"). food(f). st_hpd(enter("The couple", "new sushi place"), true, 0). st_hpd(eat("The couple", f), true, 1).
```

---

## Story #80 — Partial Match (Similarity: 0.1154)

**Story:** [REDACTED — original ROCStories text; storyid=d85b7ce5-0d84-4181-afe4-52c64711145a]

### Predicted
```clingo
restaurant("Genki Ya") at_l("Genki Ya", "Fresh Pond") at_l("Genki Ya", "Cambridge") person("I") person("my son") beverage("Japanese beer") food("fish roe") food("combo sashimi-sushi dish") st_hpd(enter("I", "Genki Ya"), true, 0) st_hpd(enter("my son", "Genki Ya"), true, 0) st_hpd(drink("I", "Japanese beer"), true, 1) st_hpd(drink("my son", "Japanese beer"), true, 1) st_hpd(eat("I", "fish roe"), true, 2) st_hpd(eat("my son", "fish roe"), true, 2) st_hpd(eat("I", "combo sashimi-sushi dish"), true, 3) st_hpd(eat("my son", "combo sashimi-sushi dish"), true, 3)
```

### Ground Truth
```clingo
restaurant("Genki Ya"). customer(we). person("my son"). person("I"). member("my son", we). member("I", we). beverage("japanese beers"). food(f). member("fish roe", f). member("sashimi-sushi dishes", f). st_hpd(enter(we, "Genki Ya"), true, 0). st_hpd(eat(we, f), true, 2). st_hpd(drink(we, "japanese beers"), true, 2).
```

---

## Story #38 — Partial Match (Similarity: 0.1176)

**Story:** One day, Andy felt hungry and went to the RRGrill restaurant for dinner. The restaurant was open and the waiter led Andy to a table. Andy went through the whole menu, but he didn't find any dish that he liked. Andy decided to leave.

### Predicted
```clingo
person("Andy"). customer("Andy"). restaurant("RRGrill"). waiter(w). st_obs(hungry("Andy"), true, 0). st_hpd(enter("Andy", "RRGrill"), true, 1). st_obs(open("RRGrill"), true, 2). st_hpd(lead_to(w, "Andy", t), true, 3). st_hpd(read_menu("Andy"), true, 4). st_hpd(leave("Andy"), true, 5).
```

### Ground Truth
```clingo
restaurant("RRGrill"). customer("Andy"). food("nothing"). waiter("the waiter"). story_step(0..4). st_hpd(enter("Andy", "RRGrill"), true, 0). st_hpd(lead_to("the waiter", "Andy", t), true, 1). st_hpd(put_down("Andy", m, t), true, 2). st_stop_activity("Andy", 3). next_st(2, 3). st_hpd(leave("Andy"), true, 4).
```

---

## Story #47 — Partial Match (Similarity: 0.1176)

**Story:** Gary went to a restaurant for his birthday. He ordered a steak. After he finished eating, the waiter surprised him with a small cake, on the house. Gary left a large tip.

### Predicted
```clingo
customer("Gary"). person("Gary"). restaurant(r). waiter(w). food("steak"). food("small cake"). st_hpd(enter("Gary", r), true, 0). st_hpd(order("Gary", "steak", w), true, 1). st_hpd(eat("Gary", "steak"), true, 2). st_obs(holding("Gary", "small cake"), true, 3). st_hpd(pay("Gary", tip), true, 4).
```

### Ground Truth
```clingo
restaurant("a restaurant"). customer("Gary"). food("steak"). food("cake"). waiter("the waiter"). story_step(0..3). st_hpd(order("Gary", "steak", "the waiter"), true, 0). st_hpd(eat("Gary", "steak"), true, 1). st_hpd(put_down("the waiter", "cake", t), true, 2). st_hpd(pay("Gary", tip), true, 3).
```

---

## Story #14 — Partial Match (Similarity: 0.1250)

**Story:** Samantha was in a five-star restaurant. Samantha started perusing the menu. She ordered the barbecued veal chop with Asian slaw and Thai fried rice.

### Predicted
```clingo
person("Samantha"). customer("Samantha"). restaurant(r). waiter(w). food("barbecued veal chop"). food("Asian slaw"). food("Thai fried rice"). st_obs(in("Samantha", r), true, 0). st_hpd(read_menu("Samantha"), true, 1). st_hpd(order("Samantha", f, w), true, 2). member("barbecued veal chop", f). member("Asian slaw", f). member("Thai fried rice", f).
```

### Ground Truth
```clingo
restaurant("a five-star restaurant"). customer("Samantha"). food("barbecued veal chop with Asian slaw and Thai fried rice"). story_step(0..2). st_obs(in("Samantha", "a five-star restaurant"), true, 0). st_hpd(read_menu("Samantha"), true, 1). st_hpd(order("Samantha", "barbecued veal chop with Asian slaw and Thai fried rice", w), true, 2).
```

---

## Story #39 — Partial Match (Similarity: 0.1250)

**Story:** One day, Andy felt hungry and went to the RRGrill restaurant for dinner. The restaurant was open. The waiter led him to a table. As Andy was sitting down before having a chance to order, he received an emergency phone call and had to leave.

### Predicted
```clingo
person("Andy"). customer("Andy"). restaurant("RRGrill"). waiter(w). st_obs(hungry("Andy"), true, 0). st_hpd(enter("Andy", "RRGrill"), true, 1). st_obs(open("RRGrill"), true, 2). st_hpd(lead_to(w, "Andy", t), true, 3). st_hpd(sit("Andy"), true, 4). st_hpd(order("Andy"), false). st_hpd(leave("Andy"), true, 5).
```

### Ground Truth
```clingo
restaurant("RRGrill"). customer("Andy"). waiter("the waiter"). story_step(0..3). st_hpd(enter("Andy", "RRGrill"), true, 0). st_hpd(lead_to("the waiter", "Andy", t), true, 1). st_obs(sitting("Andy"), true, 2). st_stop_activity("Andy", 2). st_hpd(leave("Andy"), true, 3).
```

---

## Story #48 — Partial Match (Similarity: 0.1333)

**Story:** Olivia sat down at a table. The waiter greeted her and took her drink order: a glass of water. The waiter brought the water.

### Predicted
```clingo
customer("Olivia"). person("Olivia"). waiter(w). beverage("water"). st_hpd(sit("Olivia"), true, 0). st_obs(at_l("Olivia", t), true, 0). st_hpd(greet(w, "Olivia"), true, 1). st_obs(welcomed("Olivia"), true, 1). st_hpd(order("Olivia", "water", w), true, 2). st_obs(holding("Olivia", "water"), true, 3).
```

### Ground Truth
```clingo
restaurant(r). customer("Olivia"). beverage("glass of water"). waiter("the waiter"). story_step(0..3). st_hpd(sit("Olivia"), true, 0). st_hpd(greet("the waiter", "Olivia"), true, 1). st_hpd(order("Olivia", "glass of water", "the waiter"), true, 2). st_hpd(put_down("the waiter", "glass of water", t), true, 3).
```

---

## Story #8 — Partial Match (Similarity: 0.1429)

**Story:** Derek ordered a vegetable soup. The waiter brought out the vegetable soup, but Derek was unsatisfied with the lack of vegetables in it. As an apology, the waiter decided not to charge Derek for the soup.

### Predicted
```clingo
restaurant(r). waiter(w). person("Derek"). customer("Derek"). food("vegetable soup"). st_hpd(order("Derek", "vegetable soup", w), true, 0). st_obs(served("Derek"), true, 1). st_hpd(cancel_bill(w), true, 2).
```

### Ground Truth
```clingo
restaurant("restaurant"). customer("Derek"). food("vegetable soup"). waiter("the waiter"). story_step(0..3). st_hpd(order("Derek", "vegetable soup", "the waiter"), true, 0). st_hpd(put_down("the waiter", "vegetable soup", t), true, 1). st_hpd(complain("Derek", "the waiter"), true, 2). st_next(1, 2). st_hpd(pay("derek", b), false, 3).
```

---

## Story #13 — Partial Match (Similarity: 0.1429)

**Story:** Judy looked at the menu. She and her two kids, Alex and Zoe, were seated in a booth in a local restaurant. They ordered fish and chips.

### Predicted
```clingo
person("Judy"). customer("Judy"). person("Alex"). customer("Alex"). person("Zoe"). customer("Zoe"). restaurant(r). waiter(w). food("fish and chips"). member("Judy", "group"). member("Alex", "group"). member("Zoe", "group"). st_hpd(read_menu("Judy"), true, 0). st_obs(in("Judy", r), true, 1). st_obs(in("Alex", r), true, 1). st_obs(in("Zoe", r), true, 1). st_obs(at_l("Judy", t), true, 1). st_obs(at_l("Alex", t), true, 1). st_obs(at_l("Zoe", t), true, 1). st_obs(sitting("Judy"), true, 1). st_obs(sitting("Alex"), true, 1). st_obs(sitting("Zoe"), true, 1). st_hpd(order("Judy", f, w), true, 2). member("fish and chips", f).
```

### Ground Truth
```clingo
restaurant("a local restaurant"). person("Judy"). person("Alex"). person("Zoe"). customer("they"). member("Judy", "they"). member("Alex", "they"). member("Zoe", "they"). food("fish and chips"). story_step(0..1). st_obs(sitting("they"), true, 0). st_hpd(order("they", "fish and chips", w), true, 1).
```

---

## Story #28 — Partial Match (Similarity: 0.1429)

**Story:** One day, Andy felt hungry, and went to the RRGrill restaurant for dinner. The restaurant was open, so he walked into the restaurant where he was greeted by the waiter and was led to the table. Andy ordered soup and he ate it with pleasure. He paid cash and left.

### Predicted
```clingo
person("Andy") customer("Andy") restaurant("RRGrill") waiter(w) food("soup") st_obs(hungry("Andy"), true, 0) st_obs(open("RRGrill"), true, 1) st_hpd(enter("Andy", "RRGrill"), true, 2) st_hpd(greet(w, "Andy"), true, 3) st_hpd(lead_to(w, "Andy", t), true, 4) st_hpd(order("Andy", "soup", w), true, 5) st_hpd(eat("Andy", "soup"), true, 6) st_hpd(pay("Andy", b), true, 7) st_hpd(leave("Andy"), true, 8)
```

### Ground Truth
```clingo
restaurant("RRGrill"). customer(andy). food(soup). waiter("the waiter"). story_step(0..4). st_hpd(enter(andy, "RRGrill"), true, 0). st_hpd(greet("the waiter", andy), true, 1). st_hpd(lead_to("the waiter", andy, t), true, 2). st_hpd(order(andy, soup, "the waiter"), true, 3). st_hpd(eat(andy, soup), true, 4). st_hpd(pay(andy, b), true, 5). st_hpd(leave(andy), true, 6).
```

---

## Story #83 — Partial Match (Similarity: 0.1429)

**Story:** [REDACTED — original ROCStories text; storyid=9c2ccb82-003d-4253-9f19-65b157b9993f]

### Predicted
```clingo
restaurant("the diner") waiter("the server") waiter("the waitress") person("customer1") person("customer2") st_hpd(sit("customer1"), true, 0) st_hpd(sit("customer2"), true, 0) st_hpd(stand_up("customer1"), true, 1) st_hpd(stand_up("customer2"), true, 1) st_hpd(request("the waitress", "order", "customer1"), true, 2)
```

### Ground Truth
```clingo
restaurant("diner"). customer("the couple"). waiter("the waitress"). st_hpd(sit("the couple"), true, 0). st_hpd(greet("the waitress", "the couple"), false). st_hpd(stand_up("the couple"), true, 1).
```

---

## Story #52 — Partial Match (Similarity: 0.1500)

**Story:** David walked into the seafood restaurant and was shown to his table. He browsed the menu and ordered grilled salmon with vegetables. The food arrived quickly. David ate his meal and paid the bill before leaving.

### Predicted
```clingo
customer("David"). person("David"). waiter(w). restaurant("seafood restaurant"). food("grilled salmon with vegetables"). st_hpd(enter("David","seafood restaurant"),true,0). st_hpd(lead_to(w,"David",t),true,1). st_hpd(read_menu("David"),true,2). st_hpd(order("David","grilled salmon with vegetables",w),true,3). st_obs(served("David"),true,4). st_hpd(eat("David","grilled salmon with vegetables"),true,5). st_hpd(pay("David",b),true,6). st_hpd(leave("David"),true,7).
```

### Ground Truth
```clingo
restaurant("seafood restaurant"). customer("David"). food("grilled salmon with vegetables"). waiter("the waiter"). st_hpd(enter("David", "seafood restaurant"), true, 0). st_hpd(lead_to("the waiter", "David", t), true, 1). st_hpd(order("David", "grilled salmon with vegetables", "the waiter"), true, 2). st_hpd(put_down("the waiter", "grilled salmon with vegetables", t), true, 3). st_hpd(eat("David", "grilled salmon with vegetables"), true, 4). st_hpd(pay("David", b), true, 5). st_hpd(leave("David"), true, 6).
```

---

## Story #49 — Partial Match (Similarity: 0.1538)

**Story:** The waiter brought the bill to Mark's table. Mark reviewed it and noticed he had been charged for a dessert he didn't order. He called the waiter over to correct the bill.

### Predicted
```clingo
customer("Mark"). person("Mark"). waiter(w). st_obs(at_l("Mark", t), true, 0). st_obs(bill_generated("Mark", b), true, 0). st_hpd(read_bill("Mark"), true, 1). food("dessert"). st_hpd(order("Mark", "dessert", w), false). st_hpd(request("Mark", "correct the bill", w), true, 2).
```

### Ground Truth
```clingo
restaurant(r). customer("Mark"). food("dessert"). waiter("the waiter"). st_hpd(put_down("the waiter", b, t), true, 0). st_hpd(pick_up("Mark", b, t), true, 1). st_hpd(request("Mark", "correction", "the waiter"), true, 1).
```

---

## Story #79 — Partial Match (Similarity: 0.1538)

**Story:** [REDACTED — original ROCStories text; storyid=845b62e4-9240-4afe-8d59-ae2bc183967c]

### Predicted
```clingo
restaurant("new steakhouse"). customer("the couple"). person("the couple"). food("huge cut of meat"). st_hpd(enter("the couple", "new steakhouse"), true, 0). st_hpd(order("the couple", "huge cut of meat", w), true, 1). st_hpd(order("the couple", "huge cut of meat", w), true, 2). st_obs(served("the couple"), true, 3). st_hpd(read_bill("the couple"), true, 4).
```

### Ground Truth
```clingo
restaurant("new steakhouse"). customer("the couple"). food("huge cuts of meat"). st_obs(in("the couple", "new steakhouse"), true, 0). st_hpd(put_down(w, "huge cuts of meat", t), true, 1). st_hpd(eat("the couple", "huge cuts of meat"), true, 2). st_hpd(put_down(w, b, t), true, 3).
```

---

## Story #95 — Partial Match (Similarity: 0.1579)

**Story:** [REDACTED — original ROCStories text; storyid=cd9a0a7b-ef8f-42c0-86ac-fe80542cebd3]

### Predicted
```clingo
restaurant(r). person("Austin"). waiter("the manager"). customer("the homeless man"). food("food"). food("full meal"). st_hpd(enter("the homeless man", r), true, 0). st_hpd(request("the homeless man", "food", "Austin"), true, 1). st_hpd(lead_to("the manager", "the homeless man", t), true, 2). st_hpd(sit("the homeless man"), true, 3). st_obs(served("the homeless man"), true, 4).
```

### Ground Truth
```clingo
restaurant("a restaurant"). customer("a homeless man"). waiter("wait staff"). person("Austin"). food("spare food"). food("full meal").  st_hpd(enter("a homeless man", "a restaurant"), true, 0). st_hpd(request("a homeless man", "spare food", "Austin"), true, 1). st_hpd(sit("a homeless man"), true, 2). st_hpd(put_down("wait staff", "full meal", t), true, 3). st_hpd(pay("a homeless man", b), false).
```

---

## Story #53 — Partial Match (Similarity: 0.1622)

**Story:** The Johnson family entered the family restaurant. They were seated in a booth and given menus. Mr. Johnson ordered steak, Mrs. Johnson ordered salad, and their son ordered pizza. The waiter brought all their orders together.

### Predicted
```clingo
customer("Mr. Johnson"). person("Mr. Johnson"). customer("Mrs. Johnson"). person("Mrs. Johnson"). customer("their son"). person("their son"). waiter(w). restaurant("family restaurant"). food("steak"). food("salad"). food("pizza"). st_hpd(enter("Mr. Johnson","family restaurant"),true,0). st_hpd(enter("Mrs. Johnson","family restaurant"),true,0). st_hpd(enter("their son","family restaurant"),true,0). st_hpd(lead_to(w,"Mr. Johnson",t),true,1). st_hpd(lead_to(w,"Mrs. Johnson",t),true,1). st_hpd(lead_to(w,"their son",t),true,1). st_hpd(sit("Mr. Johnson"),true,2). st_hpd(sit("Mrs. Johnson"),true,2). st_hpd(sit("their son"),true,2). st_hpd(order("Mr. Johnson","steak",w),true,3). st_hpd(order("Mrs. Johnson","salad",w),true,3). st_hpd(order("their son","pizza",w),true,3). st_obs(served("Mr. Johnson"),true,4). st_obs(served("Mrs. Johnson"),true,4). st_obs(served("their son"),true,4).
```

### Ground Truth
```clingo
restaurant("family restaurant"). person("Mr. Johnson"). person("Mrs. Johnson"). person("son"). customer("Johnson family"). member("Mr. Johnson", "Johnson family"). member("Mrs. Johnson", "Johnson family"). member("son", "Johnson family"). food("steak"). food("salad"). food("pizza"). waiter("the waiter"). story_step(0..4). st_hpd(enter("Johnson family", "family restaurant"), true, 0). st_obs(sitting("Johnson family"), true, 1). st_hpd(order("Mr. Johnson", "steak", "the waiter"), true, 2). st_hpd(order("Mrs. Johnson", "salad", "the waiter"), true, 2). st_hpd(order("son", "pizza", "the waiter"), true, 2). st_hpd(put_down("the waiter", "steak", t), true, 3). st_hpd(put_down("the waiter", "salad", t), true, 3). st_hpd(put_down("the waiter", "pizza", t), true, 3).
```

---

## Story #78 — Partial Match (Similarity: 0.1667)

**Story:** [REDACTED — original ROCStories text; storyid=02fbf49d-54f4-493d-b4af-609cc1e23a22]

### Predicted
```clingo
restaurant("diner"). customer("Betsy"). person("Betsy"). waiter("the waitress"). food("greasy breakfast"). food("pancakes"). food("bacon"). beverage("coffee"). st_obs(available("greasy breakfast", "diner"), true, 0). st_hpd(enter("Betsy", "diner"), true, 1). st_hpd(order("Betsy", "pancakes", "the waitress"), true, 2). st_hpd(order("Betsy", "bacon", "the waitress"), true, 3). st_hpd(order("Betsy", "coffee", "the waitress"), true, 4). st_hpd(eat("Betsy", "pancakes"), true, 5). st_hpd(eat("Betsy", "bacon"), true, 6). st_hpd(drink("Betsy", "coffee"), true, 7). st_hpd(pay("Betsy", tip), true, 8).
```

### Ground Truth
```clingo
restaurant("a diner"). customer("Betsy"). food(f). member("pancakes", f). member("bacon", f). beverage("coffee"). waiter("the waitress"). st_hpd(order("Betsy", f, "the waitress"), true, 0). st_hpd(order("Betsy", "coffee", "the waitress"), true, 0). st_hpd(eat("Betsy", f), true, 1). st_hpd(drink("Betsy", "coffee"), true, 1). st_hpd(pay("Betsy", tip), true, 2).
```

---

## Story #93 — Partial Match (Similarity: 0.1667)

**Story:** [REDACTED — original ROCStories text; storyid=0b8e4ddd-6ada-42ba-9d6f-508db0bac85a]

### Predicted
```clingo
customer("I"). customer("my mother"). restaurant(r). waiter(w). food("steak"). restaurant("Burger King"). st_hpd(enter("I", r), true, 0). st_hpd(enter("my mother", r), true, 0). st_hpd(sit("I"), true, 1). st_hpd(sit("my mother"), true, 1). st_hpd(order("I", "steak", w), true, 2). st_obs(available("steak", r), false, 3). st_obs(informed(w, "they are out of steak", "I"), true, 3). st_hpd(leave("I"), true, 4). st_hpd(leave("my mother"), true, 4). st_hpd(enter("I", "Burger King"), true, 5). st_hpd(enter("my mother", "Burger King"), true, 5).
```

### Ground Truth
```clingo
restaurant("the restaurant"). restaurant("Burger King"). customer(we). person("I"). person("my mother"). food("steak"). st_hpd(sit(we), true, 0). st_hpd(order("I", "steak", w), true, 1). st_obs(available("steak", "the restaurant"), false, 1). st_hpd(leave(we), true, 2). st_hpd(enter(we, "Burger King"), true, 3).
```

---

## Story #51 — Partial Match (Similarity: 0.1739)

**Story:** Steve and his son entered a pizzeria. The waiter took them to a table by the window. They ordered a large pepperoni pizza to share. After eating, Steve paid the bill.

### Predicted
```clingo
customer("Steve"). person("Steve"). customer("his son"). person("his son"). waiter(w). restaurant("pizzeria"). food("large pepperoni pizza"). member("Steve", g). member("his son", g). member("large pepperoni pizza", g). st_hpd(enter("Steve","pizzeria"),true,0). st_hpd(enter("his son","pizzeria"),true,0). st_hpd(lead_to(w,"Steve",t),true,1). st_hpd(lead_to(w,"his son",t),true,1). st_hpd(order("Steve","large pepperoni pizza",w),true,2). st_hpd(pay("Steve",b),true,3).
```

### Ground Truth
```clingo
restaurant("pizzeria"). customer(they). person("Steve"). person("his son"). member("Steve", they). member("his son", they). food("large pepperoni pizza"). waiter("the waiter"). story_step(0..4). st_hpd(enter(they, "pizzeria"), true, 0). st_hpd(lead_to("the waiter", they, t), true, 1). st_hpd(order(they, "large pepperoni pizza", "the waiter"), true, 2). st_hpd(eat(they, "large pepperoni pizza"), true, 3). st_hpd(pay("Steve", b), true, 4).
```

---

## Story #3 — Partial Match (Similarity: 0.1765)

**Story:** Jill enters the restaurant and is escorted to a table. She orders chicken. The waiter brings the chicken to her table. After eating, Jill asks for the bill.

### Predicted
```clingo
restaurant(r). waiter(w). person("Jill"). customer("Jill"). food("chicken"). st_hpd(enter("Jill", r), true, 0). st_hpd(lead_to(w, "Jill", t), true, 1). st_hpd(order("Jill", "chicken", w), true, 2). st_obs(served("Jill"), true, 3). st_hpd(eat("Jill", "chicken"), true, 4). st_hpd(request("Jill", b, w), true, 5).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer("Jill"). food("chicken"). waiter("the waiter"). story_step(0..5). st_hpd(enter("Jill", "the restaurant"), true, 0). st_hpd(lead_to("the waiter", "Jill", t), true, 1). st_hpd(order("Jill", "chicken", "the waiter"), true, 2). st_hpd(put_down("the waiter", "chicken", t), true, 3). st_hpd(eat("Jill", "chicken"), true, 4). st_hpd(request("Jill", b, "the waiter"), true, 5).
```

---

## Story #5 — Partial Match (Similarity: 0.1765)

**Story:** The waiter shows Jane to her table. Jane is seated at a table in the restaurant. The waiter asks for her order, and she orders fish. After eating, the waiter brings the bill to the table.

### Predicted
```clingo
restaurant(r). waiter(w). person("Jane"). customer("Jane"). food("fish"). st_hpd(lead_to(w, "Jane", t), true, 0). st_obs(in("Jane", r), true, 1). st_obs(sitting("Jane"), true, 1). st_hpd(request(w, f, "Jane"), true, 2). st_hpd(order("Jane", "fish", w), true, 3). st_hpd(eat("Jane", "fish"), true, 4). st_obs(bill_generated("Jane", b), true, 5).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer("Jane"). food("fish"). waiter("the waiter"). story_step(0..4). st_hpd(lead_to("the waiter", "Jane", t), true, 0). st_obs(sitting("Jane"), true, 1). st_hpd(order("Jane", "fish", "the waiter"), true, 2). st_hpd(eat("Jane", "fish"), true, 3). st_hpd(put_down("the waiter", b, t), true, 4).
```

---

## Story #32 — Partial Match (Similarity: 0.1765)

**Story:** Nicole went to a vegetarian restaurant. She ordered a lentil soup. Nicole was in a hurry, so as soon as the waitress laid the dish on the table, Nicole paid for it in cash and said that she didn't need the bill.

### Predicted
```clingo
person("Nicole"). customer("Nicole"). restaurant(r). waiter(w). food("lentil soup"). st_hpd(enter("Nicole", r), true, 0). st_hpd(order("Nicole", "lentil soup", w), true, 1). st_hpd(put_down(w, "lentil soup", t), true, 2). st_hpd(pay("Nicole", b), true, 3). st_obs(paid(b), true, 4). st_hpd(read_bill("Nicole"), false).
```

### Ground Truth
```clingo
restaurant(veg_r). customer(nicole). person(owner). food(lentil_soup). waiter(waitress). story_step(0..3). st_hpd(enter(nicole, veg_r), true, 0). st_hpd(order(nicole, lentil_soup, waitress), true, 1). st_hpd(put_down(waitress, miso_soup, t), true, 2). st_hpd(pay(nicole, b), true, 3). next_st(2, 3).
```

---

## Story #40 — Partial Match (Similarity: 0.1765)

**Story:** Ken was at a sushi restaurant. He ordered the tuna roll. The waiter brought the tuna roll, but Ken noticed a long hair in it. He complained to the waiter, who apologized and brought a new, hair-free roll.

### Predicted
```clingo
customer("Ken"). person("Ken"). restaurant("sushi restaurant"). waiter(w). food("tuna roll"). st_obs(in("Ken", "sushi restaurant"), true, 0). st_hpd(order("Ken", "tuna roll", w), true, 1). st_obs(served("Ken"), true, 2). st_hpd(complain("Ken", w), true, 3). st_next(2, 3). st_obs(served("Ken"), true, 4).
```

### Ground Truth
```clingo
restaurant("sushi restaurant"). customer("Ken"). food("tuna roll"). food("new tuna roll"). waiter("the waiter"). story_step(0..4). st_hpd(order("Ken", "tuna roll", "the waiter"), true, 0). st_hpd(put_down("the waiter", "tuna roll", t), true, 1). st_hpd(complain("Ken", "the waiter"), true, 2). st_next(1, 2). st_hpd(put_down(w, "new tuna roll", t), true, 3).
```

---

## Story #74 — Partial Match (Similarity: 0.1786)

**Story:** Lisa and Mark went to the Italian restaurant for their date night. They were seated at a cozy table. Lisa ordered lasagna and Mark ordered chicken parmesan. They shared a bottle of wine with their meal.

### Predicted
```clingo
restaurant("Italian restaurant"). customer("Lisa"). person("Lisa"). customer("Mark"). person("Mark"). food("lasagna"). food("chicken parmesan"). beverage("bottle of wine"). st_hpd(enter("Lisa", "Italian restaurant"), true, 0). st_hpd(enter("Mark", "Italian restaurant"), true, 1). st_hpd(sit("Lisa"), true, 2). st_obs(at_l("Lisa", "cozy table"), true, 2). st_hpd(sit("Mark"), true, 3). st_obs(at_l("Mark", "cozy table"), true, 3). st_hpd(order("Lisa", "lasagna", w), true, 4). st_hpd(order("Mark", "chicken parmesan", w), true, 5). st_hpd(order("Lisa", "bottle of wine", w), true, 6). st_hpd(drink("Lisa", "bottle of wine"), true, 7). st_hpd(drink("Mark", "bottle of wine"), true, 8).
```

### Ground Truth
```clingo
restaurant("Italian restaurant"). customer("Lisa"). customer("Mark"). customer(they). member("Lisa", they). member("Mark", they). food("lasagna"). food("chicken parmesan"). beverage("wine"). st_hpd(enter(they, "Italian restaurant"), true, 0). st_obs(sitting(they), true, 1). st_hpd(order("Lisa", "lasagna", "the waiter"), true, 2). st_hpd(order("Mark", "chicken parmesan", "the waiter"), true, 2). st_hpd(eat("Lisa", "lasagna"), true, 3). st_hpd(eat("Mark", "chicken parmesan"), true, 3). st_hpd(drink(they, "wine"), true, 3).
```

---

## Story #73 — Partial Match (Similarity: 0.1818)

**Story:** David entered the deli and took a seat at the counter. He ordered a pastrami sandwich and a pickle. The cook prepared his sandwich and the server brought it to him. David ate his lunch quickly.

### Predicted
```clingo
restaurant("deli"). customer("David"). person("David"). waiter("the server"). cook("the cook"). food("pastrami sandwich"). food("pickle"). st_hpd(enter("David", "deli"), true, 0). st_hpd(sit("David"), true, 1). st_obs(at_l("David", "counter"), true, 1). st_hpd(order("David", "pastrami sandwich", "the server"), true, 2). st_hpd(order("David", "pickle", "the server"), true, 3). st_hpd(prepare("the cook", "pastrami sandwich", "the server"), true, 4). st_obs(served("David"), true, 5). st_hpd(eat("David", "pastrami sandwich"), true, 6). st_hpd(eat("David", "pickle"), true, 7).
```

### Ground Truth
```clingo
restaurant("the deli"). customer("David"). food(f). member("pastrami sandwich", f). member("pickle", f). st_hpd(enter("David", "the deli"), true, 0). st_hpd(sit("David"), true, 1). st_hpd(order("David", f, "the server"), true, 2). st_hpd(prepare("the cook", f, "the server"), true, 3). st_hpd(put_down("the server", f, t), true, 4). st_hpd(eat("David", f), true, 5).
```

---

## Story #29 — Partial Match (Similarity: 0.1875)

**Story:** Nicole went to a vegetarian restaurant. She ordered lentil soup. When the waitress brought her the soup, she told Nicole that it was on the house. Nicole enjoyed the soup and then left.

### Predicted
```clingo
person("Nicole") customer("Nicole") restaurant("vegetarian restaurant") waiter("the waitress") food("lentil soup") st_hpd(order("Nicole", "lentil soup", "the waitress"), true, 0) st_obs(served("Nicole"), true, 1) st_obs(informed("the waitress", "on the house", "Nicole"), true, 2) st_hpd(leave("Nicole"), true, 3)
```

### Ground Truth
```clingo
restaurant(veg_r). customer(nicole). person(owner). food(lentil_soup). waiter(waitress). story_step(0..5). st_hpd(enter(nicole, veg_r), true, 0). st_hpd(order(nicole, lentil_soup, waitress), true, 1). st_hpd(pay(owner, b), true, 2). st_hpd(put_down(waitress, lentil_soup, t), true, 3). st_hpd(eat(nicole, lentil_soup), true, 4). st_hpd(leave(nicole), true, 5).
```

---

## Story #36 — Partial Match (Similarity: 0.1875)

**Story:** One day, Andy felt hungry and went to the RRGrill restaurant for dinner. The restaurant was open and Tom, Andyâ€™s friend, had his birthday party in there. Tom had prepaid for all the food that was offered. The waiter led Andy to Tomâ€™s table. Andy joined the party.

### Predicted
```clingo
person("Andy"). customer("Andy"). person("Tom"). restaurant("RRGrill"). waiter(w). st_obs(hungry("Andy"), true, 0). st_hpd(enter("Andy", "RRGrill"), true, 1). st_obs(open("RRGrill"), true, 2). st_hpd(lead_to(w, "Andy", t), true, 3). st_obs(at_l("Andy", t), true, 4). st_hpd(pay("Tom", b), true, 5).
```

### Ground Truth
```clingo
restaurant("RRGrill"). customer("Andy"). person("Tom"). food("all the food"). waiter("the waiter"). story_step(0..2). st_hpd(enter("Andy", "RRGrill"), true, 0). st_hpd(lead_to("the waiter", "Andy", t), true, 1). st_obs(informed("the waiter", "all the food", "Andy"), true, 2). st_hpd(pay("Tom", b), 2).
```

---

## Story #90 — Partial Match (Similarity: 0.1875)

**Story:** [REDACTED — original ROCStories text; storyid=c4078b0f-e1c3-4c75-a05a-a52c9481fc2a]

### Predicted
```clingo
restaurant("restaurant on the Ohio river"). customer("my family"). customer("I"). food("salmon"). food("asparagus"). food("bread"). food("meal"). member("I", "my family"). st_hpd(enter("my family", "restaurant on the Ohio river"), true, 0). st_hpd(eat("I", "salmon"), true, 1). st_hpd(eat("I", "asparagus"), true, 2).
```

### Ground Truth
```clingo
restaurant("a restaurant"). customer("My family"). customer("I"). food("bread"). food("salmon and asparagus"). st_hpd(enter("My family", "a restaurant"), true, 0). st_hpd(eat("My family", "bread"), true, 1). st_hpd(eat("I", "salmon and asparagus"), true, 1).
```

---

## Story #2 — Partial Match (Similarity: 0.1905)

**Story:** John enters the restaurant. The waiter escorts him to a table. John orders steak. The waiter brings the steak to the table. John asks for the bill, and the waiter brings it to the table. John pays the bill and leaves the restaurant.

### Predicted
```clingo
restaurant(r). waiter(w). person("John"). customer("John"). food("steak"). st_hpd(enter("John", r), true, 0). st_hpd(lead_to(w, "John", t), true, 1). st_hpd(order("John", "steak", w), true, 2). st_obs(served("John"), true, 3). st_hpd(request("John", b, w), true, 4). st_obs(bill_generated("John", b), true, 5). st_hpd(pay("John", b), true, 6). st_obs(paid(b), true, 6). st_hpd(leave("John"), true, 7).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer("John"). food("steak"). waiter("the waiter"). story_step(0..6). st_hpd(enter("John", "the restaurant"), true, 0). st_hpd(lead_to("the waiter", "John", t), true, 1). st_hpd(order("John", "steak", "the waiter"), true, 2). st_hpd(put_down("the waiter", "steak", t), true, 3). st_hpd(request("John", b, "the waiter"), true, 4). st_hpd(put_down("the waiter", b, t), true, 5). st_hpd(pay("John", b), true, 6). st_hpd(leave("John"), true, 7).
```

---

## Story #9 — Partial Match (Similarity: 0.1905)

**Story:** Pete is seated at his table in the restaurant. He has ordered and received his chicken, but is unhappy with how undercooked the chicken is. He complains to the waiter, and asks for a better cooked dish.

### Predicted
```clingo
restaurant(r). waiter(w). person("Pete"). customer("Pete"). food("chicken"). food("a better cooked dish"). st_obs(in("Pete", r), true, 0). st_obs(at_l("Pete", t), true, 0). st_obs(sitting("Pete"), true, 0). st_hpd(order("Pete", "chicken", w), true, 1). st_obs(served("Pete"), true, 2). st_hpd(complain("Pete", w), true, 3). st_next(2, 3). st_hpd(request("Pete", "a better cooked dish", w), true, 4).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer("Pete"). food("chicken"). food("undercooked chicken"). food("better cooked chicken"). waiter("the waiter"). story_step(0..4). st_obs(sitting("Pete"), true, 0). st_hpd(order("Pete", "chicken", "the waiter"), true, 1). st_hpd(put_down("the waiter", "undercooked_chicken", t), true, 2). st_hpd(complain("Pete", "the waiter"), true, 3). st_next(2, 3). st_hpd(order("Pete", "better cooked chicken", "the waiter"), true, 4).
```

---

## Story #12 — Partial Match (Similarity: 0.1935)

**Story:** My husband and I went to a famous restaurant listed in our guidebook. We were seated at a booth and began studying the menu. We ordered escargot, lamb, savory salmon, and a creamy flan dessert.

### Predicted
```clingo
person("I"). customer("I"). person("my husband"). customer("my husband"). restaurant(r). waiter(w). food("escargot"). food("lamb"). food("savory salmon"). food("creamy flan dessert"). member("I", "group"). member("my husband", "group"). st_hpd(enter("I", r), true, 0). st_hpd(enter("my husband", r), true, 0). st_obs(at_l("I", t), true, 1). st_obs(at_l("my husband", t), true, 1). st_obs(sitting("I"), true, 1). st_obs(sitting("my husband"), true, 1). st_hpd(read_menu("I"), true, 2). st_hpd(read_menu("my husband"), true, 2). st_hpd(order("I", f, w), true, 3). member("escargot", f). member("lamb", f). member("savory salmon", f). member("creamy flan dessert", f).
```

### Ground Truth
```clingo
restaurant("a famous restaurant"). person("my husband"). person("I"). customer("we"). member("my husband", "we"). member("I", "we"). member("escargot", f). member("lamb", f). member("savory salmon", f). member("creamy flan dessert", f) story_step(0..3). st_hpd(enter("we", "a famous restaurant"), true, 0). st_obs(sitting("we"), true, 1). st_hpd(read_menu("we"), true, 2). st_hpd(order("we", f, w), true, 3).
```

---

## Story #11 — Partial Match (Similarity: 0.2000)

**Story:** Jake is seated at his table in the restaurant. He orders a medium-rare steak. The waiter brings out his order but it is too rare.

### Predicted
```clingo
person("Jake"). customer("Jake"). restaurant(r). waiter(w). food("medium-rare steak"). st_obs(in("Jake", r), true, 0). st_obs(at_l("Jake", t), true, 0). st_obs(sitting("Jake"), true, 0). st_hpd(order("Jake", "medium-rare steak", w), true, 1). st_hpd(put_down(w, "medium-rare steak", t), true, 2). st_obs(served("Jake"), true, 2).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer("Jake"). food("medium-rare steak"). food("too rare steak"). waiter("the waiter"). story_step(0..2). st_obs(sitting("Jake"), true, 0). st_hpd(order("Jake", "medium-rare steak", "the waiter"), true, 1). st_hpd(put_down("the waiter", "too rare steak", t), true, 2).
```

---

## Story #23 — Partial Match (Similarity: 0.2000)

**Story:** I opened the menu and chose the salmon. The waiter poured two glasses of red wine. I sipped the wine. Then our server brought a small plate of hors d'oeuvres. I tried a little bit of everything. Soon, the waiter brought the meal. I tasted the salmon.

### Predicted
```clingo
person("I") customer("I") waiter(w) person("our server") food("salmon") food("hors d'oeuvres") food("meal") beverage("red wine") st_obs(served("I"), true, 0) st_hpd(drink("I", "red wine"), true, 1) st_hpd(eat("I", "salmon"), true, 2)
```

### Ground Truth
```clingo
restaurant(r). customer("I"). food(salmon). beverage("red wine"). food("hors d'oeuvres"). waiter("the waiter"). story_step(0..7). st_hpd(pick_up("I", m, t), true, 0). st_hpd(order("I", salmon, "the waiter"), true, 1). st_hpd(put_down("I", "red wine", t), true, 2). st_hpd(drink("I", "red wine"), true, 3). st_hpd(put_down("the waiter", "hors d'oeuvres", t), true, 4). st_hpd(eat("I", "hors d'oeuvres"), true, 5). st_hpd(put_down("the waiter", salmon, t), true, 6). st_hpd(eat("I", salmon), true, 7).
```

---

## Story #30 — Partial Match (Similarity: 0.2000)

**Story:** Nicole went to a vegetarian restaurant. She ordered lentil soup. The waitress brought her a miso soup instead.

### Predicted
```clingo
person("Nicole"). customer("Nicole"). restaurant(r). waiter(w). food("lentil soup"). food("miso soup"). st_hpd(enter("Nicole", r), true, 0). st_hpd(order("Nicole", "lentil soup", w), true, 1). st_hpd(put_down(w, "miso soup", t), true, 2). st_obs(served("Nicole"), true, 3).
```

### Ground Truth
```clingo
restaurant(veg_r). customer(nicole). person(owner). food(lentil_soup). food(miso_soup). waiter(waitress). story_step(0..2). st_hpd(enter(nicole, veg_r), true, 0). st_hpd(order(nicole, lentil_soup, waitress), true, 1). st_hpd(put_down(waitress, miso_soup, t), true, 2).
```

---

## Story #42 — Partial Match (Similarity: 0.2000)

**Story:** David and his date, Sarah, went to a fancy restaurant. David ordered for both of them, choosing the duck confit. The waiter served the meal and poured them some wine. They enjoyed their dinner.

### Predicted
```clingo
customer("David"). person("David"). customer("Sarah"). person("Sarah"). restaurant("fancy restaurant"). waiter(w). food("duck confit"). beverage("wine"). member("David", "g"). member("Sarah", "g"). st_hpd(enter("David", "fancy restaurant"), true, 0). st_hpd(enter("Sarah", "fancy restaurant"), true, 0). st_hpd(order("David", "duck confit", w), true, 1). st_hpd(order_for("David", "Sarah", "duck confit", w), true, 1). st_obs(served("David"), true, 2). st_obs(served("Sarah"), true, 2). st_obs(holding("David", "wine"), true, 2). st_obs(holding("Sarah", "wine"), true, 2).
```

### Ground Truth
```clingo
restaurant("fancy restaurant"). customer(they). person("David"). person("Sarah"). member("David", they). member("Sarah", they). food("duck confit"). beverage("wine"). waiter("the waiter"). story_step(0..3). st_hpd(order_for("David", they, "duck confit", "the waiter"), true, 0). st_hpd(put_down("the waiter", "duck confit", t), true, 1). st_hpd(put_down("the waiter", "wine", t), true, 2). st_hpd(eat(they, "duck confit"), true, 3). st_hpd(drink(they, "wine"), true, 3).
```

---

## Story #55 — Partial Match (Similarity: 0.2083)

**Story:** Mark and Lisa went to their favorite sushi restaurant. They were seated at the sushi bar. Mark ordered tuna rolls and Lisa ordered salmon nigiri. The chef prepared their order in front of them.

### Predicted
```clingo
customer("Mark"). person("Mark"). customer("Lisa"). person("Lisa"). waiter(w). cook("the chef"). restaurant("their favorite sushi restaurant"). food("tuna rolls"). food("salmon nigiri"). st_hpd(enter("Mark","their favorite sushi restaurant"),true,0). st_hpd(enter("Lisa","their favorite sushi restaurant"),true,0). st_hpd(lead_to(w,"Mark",t),true,1). st_hpd(lead_to(w,"Lisa",t),true,1). st_hpd(order("Mark","tuna rolls",w),true,2). st_hpd(order("Lisa","salmon nigiri",w),true,2). st_hpd(prepare("the chef","tuna rolls",w),true,3). st_hpd(prepare("the chef","salmon nigiri",w),true,3).
```

### Ground Truth
```clingo
restaurant("sushi restaurant"). waiter(w). person("Mark"). person("Lisa"). customer("they"). member("Mark", "they"). member("Mark", "they"). food("tuna rolls"). food("salmon nigiri"). story_step(0..4). st_hpd(enter("they", "sushi restaurant"), true, 0). st_obs(sitting("they"), true, 1). st_hpd(order("Mark", "tuna rolls", w), true, 2). st_hpd(order("Lisa", "salmon nigiri", w), true, 2). st_hpd(prepare("the chef", "tuna rolls", w), true, 3). st_hpd(prepare("the chef", "salmon nigiri", w), true, 3).
```

---

## Story #77 — Partial Match (Similarity: 0.2105)

**Story:** [REDACTED — original ROCStories text; storyid=44b80dab-a351-4065-86b8-43d519dff470]

### Predicted
```clingo
restaurant("new restaurant"). customer("Karl"). person("Karl"). customer("his wife"). person("his wife"). waiter("the waiter"). st_hpd(enter("Karl", "new restaurant"), true, 0). st_hpd(enter("his wife", "new restaurant"), true, 1). st_hpd(sit("Karl"), true, 2). st_hpd(sit("his wife"), true, 3). st_hpd(order("Karl"), false). st_hpd(order("his wife"), false). st_hpd(leave("Karl"), true, 4). st_hpd(leave("his wife"), true, 5).
```

### Ground Truth
```clingo
restaurant("new restaurant"). waiter("the waiter"). customer(they). person("Karl"). person("his wife"). member("Karl", they). member("his wife", they). waiter(w). st_obs(sitting(they), true, 0). st_hpd(served(they), false, 1). st_hpd(leave(they), true, 2).
```

---

## Story #65 — Partial Match (Similarity: 0.2143)

**Story:** Maria entered the Italian restaurant and was greeted by the host. She was seated at a corner table and handed a menu. Maria ordered spaghetti carbonara and a glass of red wine. The waiter brought her order promptly. She enjoyed her meal and asked for the bill.

### Predicted
```clingo
restaurant("Italian restaurant"). host("host"). waiter(w). person("Maria"). customer("Maria"). food("spaghetti carbonara"). beverage("glass of red wine"). st_hpd(enter("Maria", "Italian restaurant"), true, 0). st_hpd(greet("host", "Maria"), true, 1). st_hpd(lead_to("host", "Maria", t), true, 2). st_hpd(sit("Maria"), true, 3). st_hpd(order("Maria", "spaghetti carbonara", w), true, 4). st_hpd(order("Maria", "glass of red wine", w), true, 5). st_obs(at_l("spaghetti carbonara", t), true, 6). st_obs(at_l("glass of red wine", t), true, 6). st_obs(served("Maria"), true, 6). st_hpd(eat("Maria", "spaghetti carbonara"), true, 7). st_hpd(drink("Maria", "glass of red wine"), true, 8). st_hpd(request("Maria", b, w), true, 9).
```

### Ground Truth
```clingo
restaurant("Italian restaurant"). customer("Maria"). person("the host"). food("spaghetti carbonara"). beverage("red wine"). waiter("the waiter"). story_step(0..6). st_hpd(enter("Maria", "Italian restaurant"), true, 0). st_hpd(greet("the host", "Maria"), true, 1). st_hpd(lead_to("the host", "Maria", t), true, 2). st_hpd(order("Maria", "spaghetti carbonara", "the waiter"), true, 3). st_hpd(order("Maria", "red wine", "the waiter"), true, 3). st_hpd(put_down("the waiter", "spaghetti carbonara", t), true, 4). st_hpd(put_down("the waiter", "red wine", t), true, 4). st_hpd(eat("Maria", "spaghetti carbonara"), true, 5). st_hpd(drink("Maria", "red wine"), true, 5). st_hpd(request("Maria", b, "the waiter"), true, 6).
```

---

## Story #84 — Partial Match (Similarity: 0.2143)

**Story:** [REDACTED — original ROCStories text; storyid=0f9b69ff-6fbe-4e94-a37a-8ef3fbf2a876]

### Predicted
```clingo
person("Donna") restaurant("the diner") at_l("the diner", "near her apartment") waiter(w) food("cheeseburger") food("onion rings") st_hpd(enter("Donna", "the diner"), true, 0) st_hpd(order("Donna", "cheeseburger", w), true, 1) st_hpd(order("Donna", "onion rings", w), true, 1)
```

### Ground Truth
```clingo
restaurant("diner"). customer("Donna"). food(f). member("cheeseburger", f). member("onion rings", f). st_hpd(enter("Donna", "diner"), true, 0). st_hpd(order("Donna", f, w), true, 1). st_hpd(eat("Donna", f), true, 2).
```

---

## Story #0 — Partial Match (Similarity: 0.2222)

**Story:** Allie enters the restaurant and claims her reservation. The waiter seats her at her table. She orders fruit salad. The waiter brings her fruit salad. After eating, she asks for the bill.

### Predicted
```clingo
restaurant(r). waiter(w). person("Allie"). customer("Allie"). food("fruit salad"). st_hpd(enter("Allie", r), true, 0). st_hpd(lead_to(w, "Allie", t), true, 1). st_hpd(sit("Allie"), true, 2). st_hpd(order("Allie", "fruit salad", w), true, 3). st_obs(served("Allie"), true, 4). st_hpd(eat("Allie", "fruit salad"), true, 5). st_hpd(request("Allie", b, w), true, 6).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer("Allie"). food("fruit salad"). waiter("the waiter"). story_step(0..6). st_hpd(enter("Allie", "the restaurant"), true, 0). st_hpd(lead_to("the waiter", "Allie", t), true, 1). st_hpd(sit("Allie"), true, 2). st_hpd(order("Allie", "fruit salad", "the waiter"), true, 3). st_hpd(put_down("the waiter", "fruit salad", t), true, 4). st_hpd(eat("Allie", "fruit salad"), true, 5). st_hpd(request("Allie", b, "the waiter"), true, 6).
```

---

## Story #31 — Partial Match (Similarity: 0.2222)

**Story:** Nicole went to a vegetarian restaurant. She ordered lentil soup. The waitress brought her a miso soup instead. Nicole decided to eat it anyway.

### Predicted
```clingo
person("Nicole"). customer("Nicole"). restaurant(r). waiter(w). food("lentil soup"). food("miso soup"). st_hpd(enter("Nicole", r), true, 0). st_hpd(order("Nicole", "lentil soup", w), true, 1). st_hpd(put_down(w, "miso soup", t), true, 2). st_obs(served("Nicole"), true, 3). st_hpd(eat("Nicole", "miso soup"), true, 4).
```

### Ground Truth
```clingo
restaurant(veg_r). customer(nicole). person(owner). food(lentil_soup). food(miso_soup). waiter(waitress). story_step(0..4). st_hpd(enter(nicole, veg_r), true, 0). st_hpd(order(nicole, lentil_soup, waitress), true, 1). st_hpd(put_down(waitress, miso_soup, t), true, 2). stop_activity(nicole, 3). next_st(2, 3). st_hpd(eat(nicole, miso_soup), true, 4).
```

---

## Story #34 — Partial Match (Similarity: 0.2222)

**Story:** One day, Andy felt hungry and went to the RRGrill restaurant for dinner. The restaurant was open, but there was no table available for Andy. Andy decided to wait. A table became available soon after.

### Predicted
```clingo
person("Andy"). customer("Andy"). restaurant("RRGrill"). st_obs(hungry("Andy"), true, 0). st_hpd(enter("Andy", "RRGrill"), true, 1). st_obs(open("RRGrill"), true, 2).
```

### Ground Truth
```clingo
restaurant("RRGrill"). customer("Andy"). story_step(0..2). st_hpd(enter("Andy", "RRGrill"), true, 0). st_obs(table_available, false, 1). st_hpd(wait("Andy"), true, 1). st_hpd(free_table, true, 2).
```

---

## Story #20 — Partial Match (Similarity: 0.2273)

**Story:** The waiter brought out escargot for Molly and me. Then the waiter brought out twelve oysters and twelve clams. We shared the clams and oysters. The waiter poured wine for us.

### Predicted
```clingo
person("Molly") person("I") customer("Molly") customer("I") waiter(w) food("escargot") food("twelve oysters") food("twelve clams") beverage("wine") member("I", "we") member("Molly", "we") member("twelve oysters", f) member("twelve clams", f) st_obs(served("I"), true, 0) st_obs(served("Molly"), true, 0)
```

### Ground Truth
```clingo
restaurant(r). customer(we). member("Molly", we). member(me, we). food(escargot). food(f). member("twelve oysters", f). member("twelve clams", f). beverage("wine"). waiter("the waiter"). story_step(0..3). st_hpd(put_down("the waiter", escargot, t), true, 0). st_hpd(put_down("the waiter", f, t), true, 1). st_hpd(eat(we, f), true, 2). st_hpd(put_down("the waiter", wine, t), true, 3).
```

---

## Story #1 — Partial Match (Similarity: 0.2308)

**Story:** Abdul is sitting in a vegetarian restaurant. The waiter takes his order, and he orders hummus. The waiter brings the hummus to the table.

### Predicted
```clingo
restaurant(r). waiter(w). person("Abdul"). customer("Abdul"). food("hummus"). st_obs(in("Abdul", r), true, 0). st_obs(sitting("Abdul"), true, 0). st_hpd(request(w, f, "Abdul"), true, 1). st_hpd(order("Abdul", "hummus", w), true, 2). st_obs(served("Abdul"), true, 3).
```

### Ground Truth
```clingo
restaurant("vegetarian restaurant"). customer("Abdul"). food("hummus"). waiter("the waiter"). story_step(0..2). st_obs(sitting("Abdul"), true, 0). st_hpd(order("Abdul", "hummus", "the waiter"), true, 1). st_hpd(put_down("the waiter", "hummus", t), true, 2).
```

---

## Story #7 — Partial Match (Similarity: 0.2308)

**Story:** Larry is seated at his table in the restaurant. The waiter brings him a menu so he can decide what to order. After reviewing the menu, Larry decides he doesn't want anything at this restaurant.

### Predicted
```clingo
restaurant(r). waiter(w). person("Larry"). customer("Larry"). st_obs(in("Larry", r), true, 0). st_obs(at_l("Larry", t), true, 0). st_obs(sitting("Larry"), true, 0). st_hpd(read_menu("Larry"), true, 1). st_obs(menu_read("Larry"), true, 2). st_hpd(order("Larry"), false).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer("Larry"). waiter("the waiter"). story_step(0..3). st_obs(sitting("Larry"), true, 0). st_hpd(put_down("the waiter", m, t), true, 1). st_obs(menu_read("Larry"), true, 2). st_hpd(order("Larry"), false, 3).
```

---

## Story #26 — Partial Match (Similarity: 0.2308)

**Story:** Nicole went to a vegetarian restaurant. She ordered lentil soup. The waitress set the soup in the middle of the table. Nicole enjoyed the soup. She left the restaurant.

### Predicted
```clingo
person("Nicole") customer("Nicole") restaurant("vegetarian restaurant") waiter("the waitress") food("lentil soup") st_hpd(order("Nicole", "lentil soup", "the waitress"), true, 0) st_obs(served("Nicole"), true, 1) st_hpd(leave("Nicole"), true, 2)
```

### Ground Truth
```clingo
restaurant(veg_r). customer(nicole). food(lentil_soup). waiter(waitress). story_step(0..4). st_hpd(enter(nicole, veg_r), true, 0). st_hpd(order(nicole, lentil_soup, waitress), true, 1). st_hpd(put_down(waitress, lentil_soup, t), true, 2). st_hpd(eat(nicole, lentil_soup), true, 3). st_hpd(leave(nicole), true, 4).
```

---

## Story #81 — Partial Match (Similarity: 0.2308)

**Story:** [REDACTED — original ROCStories text; storyid=1d235832-c133-4950-ba20-512adb2e3edb]

### Predicted
```clingo
person("Kathy") person("her friend") restaurant("the new Italian restaurant") st_obs(open("the new Italian restaurant"), true, 0) st_hpd(request("Kathy", "go with her", "her friend"), true, 0) st_hpd(enter("Kathy", "the new Italian restaurant"), true, 1) st_hpd(enter("her friend", "the new Italian restaurant"), true, 1)
```

### Ground Truth
```clingo
restaurant("new Italian restaurant"). customer(they). person("Kathy"). person("her friend"). member("Kathy", they). member("her friend", they). food("dinner"). st_hpd(enter(they, "new Italian restaurant"), true, 0). st_hpd(eat(they, "dinner"), true, 1).
```

---

## Story #15 — Partial Match (Similarity: 0.2353)

**Story:** The villager entered a fine restaurant and was seated at one of the tables. He looked at the menu. He ordered one of the items on the list. The waiter brought him a large plate of lettuce salad with several black olives on top.

### Predicted
```clingo
person("the villager"). customer("the villager"). restaurant(r). waiter(w). food("one of the items on the list"). food("lettuce salad with black olives"). st_hpd(enter("the villager", r), true, 0). st_obs(at_l("the villager", t), true, 1). st_obs(sitting("the villager"), true, 1). st_hpd(read_menu("the villager"), true, 2). st_hpd(order("the villager", "one of the items on the list", w), true, 3). st_hpd(put_down(w, "lettuce salad with black olives", t), true, 4). st_obs(served("the villager"), true, 4).
```

### Ground Truth
```clingo
restaurant("a fine restaurant"). customer("the villager"). food("one of the items on the list"). food("lettuce salad with several black olives on top"). story_step(0..4). st_hpd(enter("the villager", "a fine restaurant"), true, 0). st_obs(sitting("the villager"), true, 1). st_hpd(pick_up("the villager", m, t), true, 2). st_hpd(order("the villager", "one of the items on the list", w), true, 3). st_hpd(put_down(w, "lettuce salad with several black olives on top", t), true, 4).
```

---

## Story #25 — Partial Match (Similarity: 0.2353)

**Story:** I was the first person to appear at the restaurant. I took my seat at the middle of the table. The head-waiter waited on me himself. I had a capital dinner. Then Uncle Chipperton entered. He paid for the whole dinner.

### Predicted
```clingo
person("I") person("Uncle Chipperton") customer("I") customer("Uncle Chipperton") restaurant(r) waiter("the head-waiter") food("dinner") st_obs(in("I", r), true, 0) st_hpd(sit("I"), true, 1) st_obs(served("I"), true, 2) st_hpd(enter("Uncle Chipperton", r), true, 3) st_hpd(pay("Uncle Chipperton", b), true, 4)
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer("I"). waiter("head-waiter") food("capital dinner"). person("Uncle Chipperton"). story_step(0..5). st_hpd(enter("I", "the restaurant"), true, 0). st_hpd(sit("I"), true, 1). st_hpd(put_down("head-waiter", "capital dinner", t), true, 2). st_hpd(eat("I", "capital dinner"), true, 3). st_hpd(enter("Uncle Chipperton", "the restaurant"), true, 4). st_hpd(pay("Uncle Chipperton", b), true, 5).
```

---

## Story #60 — Partial Match (Similarity: 0.2353)

**Story:** Robert ordered a medium-rare steak but received a well-done one. He called the waiter and complained about the mistake. The waiter apologized and took the steak back to the kitchen.

### Predicted
```clingo
person("Robert"). customer("Robert"). waiter(w). food("medium-rare steak"). food("well-done steak"). st_hpd(order("Robert", "medium-rare steak", w), true, 0). st_obs(at_l("well-done steak", t), true, 1). st_obs(served("Robert"), true, 1). st_hpd(complain("Robert", w), true, 2). st_next(1, 2). st_hpd(pick_up(w, "well-done steak", t), true, 3). st_hpd(move(w, t, "kitchen"), true, 4).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer("Robert"). food("medium-rare steak"). food("well-done steak"). waiter("the waiter"). story_step(0..3). st_hpd(order("Robert", "medium-rare steak", "the waiter"), true, 0). st_hpd(put_down("the waiter", "well-done steak", t), true, 1). st_hpd(complain("Robert", "the waiter"), true, 2). st_next(1, 2). st_hpd(pick_up("the waiter", "well-done steak", t), true, 3).
```

---

## Story #4 — Partial Match (Similarity: 0.2500)

**Story:** Bob is seated at a table in the restaurant. The waiter asks for his order, and he orders a hamburger.

### Predicted
```clingo
restaurant(r). waiter(w). person("Bob"). customer("Bob"). food("hamburger"). st_obs(in("Bob", r), true, 0). st_obs(at_l("Bob", t), true, 0). st_obs(sitting("Bob"), true, 0). st_hpd(request(w, f, "Bob"), true, 1). st_hpd(order("Bob", "hamburger", w), true, 2).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer("Bob"). food("hamburger"). waiter("the waiter"). story_step(0..1). st_obs(sitting("Bob"), true, 0). st_hpd(order("Bob", "hamburger", "the waiter"), true, 1).
```

---

## Story #16 — Partial Match (Similarity: 0.2500)

**Story:** The waiter took Gavin and Amandine to a booth. They slid onto brown vinyl seats. Gavin glanced over his menu. Amandine didn't need to look to know what she wanted. She ordered egg drop soup with wonton, lobster Cantonese and shrimp, beef and pork fried rice. Gavin ordered the same.

### Predicted
```clingo
person("Gavin"). customer("Gavin"). person("Amandine"). customer("Amandine"). waiter(w). food("egg drop soup with wonton"). food("lobster Cantonese"). food("shrimp"). food("beef and pork fried rice"). member("Gavin", "group"). member("Amandine", "group"). st_hpd(lead_to(w, "Gavin", t), true, 0). st_hpd(lead_to(w, "Amandine", t), true, 0). st_hpd(sit("Gavin"), true, 1). st_hpd(sit("Amandine"), true, 1). st_hpd(read_menu("Gavin"), true, 2). st_hpd(order("Amandine", f, w), true, 3). member("egg drop soup with wonton", f). member("lobster Cantonese", f). member("shrimp", f). member("beef and pork fried rice", f). st_hpd(order("Gavin", f, w), true, 4).
```

### Ground Truth
```clingo
waiter("the waiter"). customer("Gavin"). customer("Amandine"). food(f). member("egg drop soup with wonton", f). member("lobster Cantonese", f). member("shrimp, beef and pork fried rice", f). story_step(0..4). st_hpd(lead_to("the waiter", "Gavin", t), true, 0). st_hpd(lead_to("the waiter", "Amandine", t), true, 0). st_hpd(sit("Gavin"), true, 1). st_hpd(sit("Amandine"), true, 1). st_hpd(read_menu("Gavin"), true, 2). st_hpd(read_menu("Amandine"), false). st_hpd(order("Amandine", f, "the waiter"), true, 3). st_hpd(order("Gavin", f, "the waiter"), true, 4).
```

---

## Story #56 — Partial Match (Similarity: 0.2500)

**Story:** Anna visited the vegan restaurant downtown. She ordered the quinoa bowl and a green smoothie. The food was fresh and delicious. She left a generous tip for the excellent service.

### Predicted
```clingo
customer("Anna"). person("Anna"). waiter(w). restaurant("vegan restaurant downtown"). food("quinoa bowl"). beverage("green smoothie"). st_hpd(enter("Anna","vegan restaurant downtown"),true,0). st_hpd(order("Anna","quinoa bowl",w),true,1). st_hpd(order("Anna","green smoothie",w),true,1). st_hpd(pay("Anna",tip),true,2).
```

### Ground Truth
```clingo
restaurant("vegan restaurant"). customer("Anna"). food("quinoa bowl"). beverage("green smoothie"). waiter(w). story_step(0..4). st_hpd(enter("Anna", "vegan restaurant"), true, 0). st_hpd(order("Anna", "quinoa bowl", w), true, 1). st_hpd(order("Anna", "green smoothie", w), true, 1). st_hpd(eat("Anna", "quinoa bowl"), true, 3). st_hpd(drink("Anna", "green smoothie"), true, 3). st_hpd(pay("Anna", tip), true, 4).
```

---

## Story #58 — Partial Match (Similarity: 0.2500)

**Story:** Ben went to the diner for breakfast. He sat at the counter and ordered pancakes with bacon and coffee. The cook prepared his order right in front of him.

### Predicted
```clingo
customer("Ben"). person("Ben"). waiter(w). cook("the cook"). restaurant("diner"). food("pancakes with bacon"). beverage("coffee"). st_hpd(enter("Ben","diner"),true,0). st_hpd(sit("Ben"),true,1). st_hpd(order("Ben","pancakes with bacon",w),true,2). st_hpd(order("Ben","coffee",w),true,2). st_hpd(prepare("the cook","pancakes with bacon",w),true,3).
```

### Ground Truth
```clingo
restaurant("the diner"). customer("Ben"). food("pancakes with bacon"). beverage("coffee"). story_step(0..3). st_hpd(enter("Ben", "the diner"), true, 0). st_hpd(sit("Ben"), true, 1). st_hpd(order("Ben", "pancakes with bacon", w), true, 2). st_hpd(prepare("the cook", "pancakes with bacon", w), true, 3). st_hpd(prepare("the cook", "coffee", "Ben"), true, 3).
```

---

## Story #62 — Partial Match (Similarity: 0.2500)

**Story:** The waiter at the steakhouse brought a rare steak for Wendy, but she had ordered it well-done. She sent it back to the kitchen to be cooked more.

### Predicted
```clingo
restaurant("steakhouse"). waiter(w). person("Wendy"). customer("Wendy"). food("rare steak"). food("well-done steak"). st_hpd(order("Wendy", "well-done steak", w), true, 0). st_obs(at_l("rare steak", t), true, 1). st_obs(served("Wendy"), true, 1). st_hpd(request("Wendy", "send_back", w), true, 2). st_hpd(pick_up(w, "rare steak", t), true, 3). st_hpd(move(w, t, "kitchen"), true, 4).
```

### Ground Truth
```clingo
restaurant("the steakhouse"). customer("Wendy"). food("rare steak"). food("well-done steak"). waiter("the waiter"). story_step(0..2). st_hpd(order("Wendy", "well-done steak", "the waiter"), true, 0). st_hpd(put_down("the waiter", "rare steak", t), true, 1). st_hpd(request("Wendy", pick_up("the waiter", "rare steak", t), "the waiter"), true, 2). st_next(1, 2).
```

---

## Story #66 — Partial Match (Similarity: 0.2632)

**Story:** Charlie entered a restaurant and was led to a table. He ordered a burger. The waiter brought the burger. Charlie ate it, asked for the bill, paid, and left.

### Predicted
```clingo
person("Charlie"). customer("Charlie"). waiter(w). food("burger"). st_hpd(enter("Charlie", r), true, 0). st_hpd(lead_to(w, "Charlie", t), true, 1). st_hpd(order("Charlie", "burger", w), true, 2). st_obs(at_l("burger", t), true, 3). st_obs(served("Charlie"), true, 3). st_hpd(eat("Charlie", "burger"), true, 4). st_hpd(request("Charlie", b, w), true, 5). st_hpd(pay("Charlie", b), true, 6). st_hpd(leave("Charlie"), true, 7).
```

### Ground Truth
```clingo
restaurant("a restaurant"). customer("Charlie"). food("burger"). waiter("the waiter"). story_step(0..7). st_hpd(enter("Charlie", "a restaurant"), true, 0). st_hpd(lead_to("the waiter", "Charlie", t), true, 1). st_hpd(order("Charlie", "burger", "the waiter"), true, 2). st_hpd(put_down("the waiter", "burger", t), true, 3). st_hpd(eat("Charlie", "burger"), true, 4). st_hpd(request("Charlie", b, "the waiter"), true, 5). st_hpd(pay("Charlie", b), true, 6). st_hpd(leave("Charlie"), true, 7).
```

---

## Story #87 — Partial Match (Similarity: 0.2727)

**Story:** [REDACTED — original ROCStories text; storyid=7dc0c96f-dd24-4561-9a4f-bd1b6b3ca520]

### Predicted
```clingo
person("I") restaurant("the restaurant") waiter(w) st_hpd(enter("I", "the restaurant"), true, 0) st_obs(served("I"), true, 1) st_hpd(request("I", "return the order", w), true, 2)
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer("I"). food("wrong order"). st_hpd(enter("I", "the restaurant"), true, 0). st_hpd(order("I", f, w), true, 1). st_hpd(put_down(w, "wrong order", t), true, 2). st_hpd(request("I", pick_up(w, "burnt pizza", t), w), true, 3). st_next(2,3).
```

---

## Story #88 — Partial Match (Similarity: 0.2727)

**Story:** [REDACTED — original ROCStories text; storyid=3a66621b-9dcf-4e32-b085-e4c0a2e89f8f]

### Predicted
```clingo
person("I") restaurant("the little deli on the corner") waiter(w) food("turkey sandwich") st_obs(hungry("I"), true, 0) st_hpd(enter("I", "the little deli on the corner"), true, 1) st_hpd(order("I", "turkey sandwich", w), true, 2) st_hpd(eat("I", "turkey sandwich"), true, 3)
```

### Ground Truth
```clingo
restaurant("little deli"). customer("I"). food("turkey sandwich"). st_obs(hungry("I"), true, 0). st_hpd(order("I", "turkey sandwich", w), true, 1). st_hpd(eat("I", "turkey sandwich"), true, 2).
```

---

## Story #57 — Partial Match (Similarity: 0.2778)

**Story:** Carlos arrived at the Mexican restaurant and was greeted warmly. He ordered tacos and a margarita. The food arrived quickly and was perfectly prepared. Carlos enjoyed his meal thoroughly.

### Predicted
```clingo
customer("Carlos"). person("Carlos"). waiter(w). restaurant("Mexican restaurant"). food("tacos"). beverage("margarita"). st_hpd(enter("Carlos","Mexican restaurant"),true,0). st_hpd(greet(w,"Carlos"),true,1). st_hpd(order("Carlos","tacos",w),true,2). st_hpd(order("Carlos","margarita",w),true,2). st_obs(served("Carlos"),true,3).
```

### Ground Truth
```clingo
restaurant("Mexican restaurant"). customer("Carlos"). waiter(w). food("tacos"). beverage("margarita"). story_step(0..4). st_hpd(enter("Carlos", "Mexican restaurant"), true, 0). st_hpd(greet(w, "Carlos"), true, 1). st_hpd(order("Carlos", "tacos", w), true, 2). st_hpd(order("Carlos", "margarita", w), true, 2). st_hpd(put_down(w, "tacos", t), true, 3). st_hpd(put_down(w, "margarita", t), true, 3). st_hpd(eat("Carlos", "tacos"), true, 4). st_hpd(drink("Carlos", "margarita"), true, 4).
```

---

## Story #75 — Partial Match (Similarity: 0.2778)

**Story:** [REDACTED — original ROCStories text; storyid=99d073a9-375a-45ad-a070-0fdfbbf73f69]

### Predicted
```clingo
restaurant("new Sushi place"). customer("I"). person("I"). customer("my husband"). person("my husband"). food("spicy tuna rolls"). food("eel"). st_hpd(enter("I", "new Sushi place"), true, 0). st_hpd(enter("my husband", "new Sushi place"), true, 1). st_hpd(order("I", "spicy tuna rolls", w), true, 2). st_hpd(order("I", "eel", w), true, 3). member("spicy tuna rolls", f). member("eel", f).
```

### Ground Truth
```clingo
restaurant("new Sushi place"). customer(we). person("I"). person("my husband"). member("I", we). member("my husband", we). food(f). member("spicy tuna rolls", f). member("eel", f). st_hpd(enter(we, "new Sushi place"), true, 0). st_hpd(order(we, f, w), true, 1). st_hpd(eat(we, f), true, 2).
```

---

## Story #6 — Partial Match (Similarity: 0.2857)

**Story:** Molly is seated at her table when the waiter asks for her order. She orders a baked potato. The waiter brings out French fries.

### Predicted
```clingo
restaurant(r). waiter(w). person("Molly"). customer("Molly"). food("baked potato"). food("French fries"). st_obs(at_l("Molly", t), true, 0). st_obs(sitting("Molly"), true, 0). st_hpd(request(w, f, "Molly"), true, 1). st_hpd(order("Molly", "baked potato", w), true, 2). st_obs(at_l("French fries", t), true, 3).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer("Molly"). food("baked potato"). food("French fries"). waiter("the waiter"). story_step(0..2). st_obs(sitting("Molly"), true, 0). st_hpd(order("Molly", "baked potato", "the waiter"), true, 1). st_hpd(put_down("the waiter", "French fries", t), true, 2).
```

---

## Story #33 — Partial Match (Similarity: 0.2857)

**Story:** One day, Andy felt hungry and went to the RRGrill restaurant for dinner. The restaurant was open, but there was no table available for Andy.

### Predicted
```clingo
person("Andy"). customer("Andy"). restaurant("RRGrill"). st_obs(hungry("Andy"), true, 0). st_hpd(enter("Andy", "RRGrill"), true, 1). st_obs(open("RRGrill"), true, 2).
```

### Ground Truth
```clingo
restaurant("RRGrill"). customer("Andy"). story_step(0..1). st_hpd(enter("Andy", "RRGrill"), true, 0). st_obs(table_available, false, 1).
```

---

## Story #44 — Partial Match (Similarity: 0.2857)

**Story:** At an Italian restaurant, Chloe ordered lasagna. The waiter brought her spaghetti instead. Chloe informed the waiter of the mistake.

### Predicted
```clingo
customer("Chloe"). person("Chloe"). restaurant("Italian restaurant"). waiter(w). food("lasagna"). food("spaghetti"). st_obs(in("Chloe", "Italian restaurant"), true, 0). st_hpd(order("Chloe", "lasagna", w), true, 1). st_obs(holding("Chloe", "spaghetti"), true, 2). st_obs(informed("Chloe", "the mistake", w), true, 3).
```

### Ground Truth
```clingo
restaurant("Italian restaurant"). customer("Chloe"). food("lasagna"). food("spaghetti"). waiter("the waiter"). story_step(0..2). st_hpd(order("Chloe", "lasagna", "the waiter"), true, 0). st_hpd(put_down("the waiter", "spaghetti", t), true, 1). st_hpd(complain("Chloe", "the waiter"), true, 2). st_next(1, 2).
```

---

## Story #76 — Partial Match (Similarity: 0.2857)

**Story:** [REDACTED — original ROCStories text; storyid=6ead4a09-8e5f-4fbc-8a32-b706bdbb7a87]

### Predicted
```clingo
restaurant("Allston Diner"). customer("we"). person("we"). customer("our son"). person("our son"). food("large, hearty breakfast meals"). food("dinner"). st_hpd(enter("we", "Allston Diner"), true, 0). st_hpd(enter("our son", "Allston Diner"), true, 1). st_hpd(eat("we", "large, hearty breakfast meals"), true, 2). st_hpd(eat("we" , "dinner"), false).
```

### Ground Truth
```clingo
restaurant("Allston Diner"). customer(we). person("our son"). customer("a friend"). member("our son", we). food("breakfast meals"). st_hpd(enter(we, "Allston Diner"), true, 0). st_hpd(eat(we, "breakfast meals"), true, 1). st_hpd(eat("a friend", "breakfast meals"), true, 1).
```

---

## Story #89 — Partial Match (Similarity: 0.2857)

**Story:** [REDACTED — original ROCStories text; storyid=c93ca5db-716f-4572-868e-bd22aa4a9018]

### Predicted
```clingo
person("my son") person("me") person("my wife") restaurant("Genki Ya") at_l("Genki Ya", "Fresh Pond") food("sashimi") st_hpd(enter("my son", "Genki Ya"), true, 0) st_hpd(enter("me", "Genki Ya"), true, 0) st_hpd(eat("me", "sashimi"), true, 1)
```

### Ground Truth
```clingo
restaurant("Genki Ya"). customer(we). person("my son"). person("me"). member("my son", we). member("me", we). food("sashimi"). st_hpd(enter(we, "Genki Ya"), true, 0). st_hpd(eat(we, "sashimi"), true, 1).
```

---

## Story #97 — Partial Match (Similarity: 0.2857)

**Story:** [REDACTED — original ROCStories text; storyid=d25ec012-9f9f-48e6-8274-e6ac4a4b59e4]

### Predicted
```clingo
customer("Tim"). restaurant(r). waiter(w). food("the dish served"). st_obs(in("Tim", r), true, 0). st_obs(served("Tim"), true, 1). st_hpd(order("Tim", "the dish served", w), false). st_hpd(complain("Tim", w), true, 2). st_next(1, 2).
```

### Ground Truth
```clingo
restaurant(r). customer("Tim"). food("wrong order"). waiter("the waiter"). st_obs(in("Tim", r), true, 0). st_hpd(put_down("the waiter", "wrong order", t), true, 1). st_hpd(complain("Tim", "the waiter"), true, 2). st_next(1, 2). st_hpd(put_down("the waiter", f, t), true, 3).
```

---

## Story #27 — Partial Match (Similarity: 0.2941)

**Story:** Nicole and Sam went to a vegetarian restaurant. She ordered a lentil soup. He ordered a miso soup. They both enjoyed their soups.

### Predicted
```clingo
person("Nicole") person("Sam") customer("Nicole") customer("Sam") restaurant("vegetarian restaurant") waiter(w) food("lentil soup") food("miso soup") member("Nicole", "they") member("Sam", "they") st_hpd(order("Nicole", "lentil soup", w), true, 0) st_hpd(order("Sam", "miso soup", w), true, 1)
```

### Ground Truth
```clingo
restaurant(veg_r). customer(nicole). customer(sam). food(lentil_soup). food(miso_soup). waiter(w). story_step(0..3). st_hpd(enter(nicole, veg_r), true, 0). st_hpd(enter(sam, veg_r), true, 0). st_hpd(order(nicole, lentil_soup, waitress), true, 1). st_hpd(order(sam, miso_soup, waitress), true, 2). st_hpd(eat(nicole, lentil_soup), true, 3). st_hpd(eat(sam, miso_soup), true, 3).
```

---

## Story #43 — Partial Match (Similarity: 0.2941)

**Story:** Megan entered the restaurant and sat at the bar. She ordered a glass of wine from the bartender. She finished her drink, paid the bartender, and left.

### Predicted
```clingo
customer("Megan"). person("Megan"). restaurant(r). waiter("the bartender"). beverage("wine"). st_hpd(enter("Megan", r), true, 0). st_hpd(sit("Megan"), true, 1). st_obs(at_l("Megan", "bar"), true, 1). st_hpd(order("Megan", "wine", "the bartender"), true, 2). st_hpd(drink("Megan", "wine"), true, 3). st_hpd(pay("Megan", b), true, 4). st_obs(paid(b), true, 4). st_hpd(leave("Megan"), true, 5).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer("Megan"). beverage("glass of wine"). waiter("the bartender"). st_hpd(enter("Megan", "the restaurant"), true, 0). st_hpd(sit("Megan"), true, 1). st_hpd(order("Megan", "glass of wine", "the bartender"), true, 2). st_hpd(drink("Megan", "glass of wine"), true, 3). st_hpd(pay("Megan", b), true, 4). st_hpd(leave("Megan"), true, 5).
```

---

## Story #54 — Partial Match (Similarity: 0.2941)

**Story:** Sarah visited the cafe for lunch. She sat at a table by the window and ordered a chicken sandwich and coffee. The waitress brought her order. Sarah ate quickly as she was in a hurry.

### Predicted
```clingo
customer("Sarah"). person("Sarah"). waiter("the waitress"). restaurant("cafe"). food("chicken sandwich"). beverage("coffee"). st_hpd(enter("Sarah","cafe"),true,0). st_hpd(sit("Sarah"),true,1). st_hpd(order("Sarah","chicken sandwich","the waitress"),true,2). st_hpd(order("Sarah","coffee","the waitress"),true,2). st_obs(served("Sarah"),true,3). st_hpd(eat("Sarah","chicken sandwich"),true,4).
```

### Ground Truth
```clingo
restaurant("the cafe"). customer("Sarah"). food("chicken sandwich"). beverage("coffee"). waiter("the waitress"). story_step(0..4). st_hpd(enter("Sarah", "the cafe"), true, 0). st_hpd(sit("Sarah"), true, 1). st_hpd(order("Sarah", "chicken sandwich", "the waitress"), true, 2). st_hpd(put_down("the waitress", "chicken sandwich", t), true, 3). st_hpd(eat("Sarah", "chicken sandwich"), true, 4). st_hpd(drink("Sarah", "coffee"), true, 4).
```

---

## Story #91 — Partial Match (Similarity: 0.2941)

**Story:** [REDACTED — original ROCStories text; storyid=ac7250f9-d416-41bb-aac7-b1dd788b86fb]

### Predicted
```clingo
customer("Emily"). restaurant("fast food restaurant"). waiter("the cashier"). food("fries"). food("burger"). st_hpd(enter("Emily", "fast food restaurant"), true, 0). st_hpd(order("Emily", "fries", "the cashier"), true, 1). st_hpd(order("Emily", "burger", "the cashier"), true, 2). st_obs(served("Emily"), true, 3). st_hpd(complain("Emily", "the cashier"), true, 4). st_next(3, 4).
```

### Ground Truth
```clingo
restaurant("fast food restaurant"). customer("Emily"). food("fries"). food("burger"). waiter("the cashier"). st_hpd(order("Emily", "fries", "the cashier"), true, 0). st_hpd(order("Emily", "burger", "the cashier"), true, 0). st_hpd(put_down("the cashier", "burger", t), true, 1). st_hpd(put_down("the cashier", "fries", t), false). st_hpd(complain("Emily", "the cashier"), true, 2). st_next(1,2).
```

---

## Story #37 — Partial Match (Similarity: 0.3000)

**Story:** One day, Andy felt hungry and went to the RRGrill restaurant for dinner. The restaurant was closed that day. He decided to go to Happy Pizza instead.

### Predicted
```clingo
person("Andy"). customer("Andy"). restaurant("RRGrill"). restaurant("Happy Pizza"). st_obs(hungry("Andy"), true, 0). st_hpd(enter("Andy", "RRGrill"), true, 1). st_obs(open("RRGrill"), false, 2). st_hpd(enter("Andy", "Happy Pizza"), true, 3).
```

### Ground Truth
```clingo
restaurant("RRGrill"). restaurant("Happy Pizza"). customer("Andy"). story_step(0..2). st_obs(closed("RRGrill"), true, 0). stop_activity("Andy", 1). st_hpd(move("Andy", "RRGrill", "Happy Pizza"), true, 2).
```

---

## Story #22 — Partial Match (Similarity: 0.3043)

**Story:** Andrew was sitting in a restaurant. Sebastian entered the restaurant and sat down opposite Andrew. The waiter brought a bottle of wine. Andrew and Sebastian took a drink. The waiter gave the men a menu.

### Predicted
```clingo
person("Andrew") person("Sebastian") customer("Andrew") customer("Sebastian") waiter(w) restaurant(r) beverage("wine") member("Andrew", "the men") member("Sebastian", "the men") st_obs(in("Andrew", r), true, 0) st_obs(sitting("Andrew"), true, 0) st_hpd(enter("Sebastian", r), true, 1) st_hpd(sit("Sebastian"), true, 2) st_obs(served("Andrew"), true, 3) st_obs(served("Sebastian"), true, 3) st_hpd(drink("Andrew", "wine"), true, 4) st_hpd(drink("Sebastian", "wine"), true, 4)
```

### Ground Truth
```clingo
restaurant("a restaurant"). customer("the men"). person("Andrew"). person("Sebastian"). member("Andrew", "the men"). member("Sebastian", "the men"). beverage(wine). waiter("the waiter"). story_step(0..5). st_obs(in("Andrew", "a restaurant"), true, 0). st_obs(sitting("Andrew"), true, 0). st_hpd(enter("Sebastian", "a restaurant"), true, 1). st_hpd(sit("Sebastian"), true, 2). st_hpd(put_down("the waiter", wine, t), true, 3). st_hpd(drink("the men", wine), true, 4). st_hpd(put_down("the waiter", m, t), true, 5).
```

---

## Story #50 — Partial Match (Similarity: 0.3077)

**Story:** Fiona ordered the soup of the day. The waiter returned a minute later to inform her that they had just run out of the soup. Fiona then ordered a sandwich instead.

### Predicted
```clingo
customer("Fiona"). person("Fiona"). waiter(w). restaurant(r). food("soup of the day"). food("sandwich"). st_hpd(order("Fiona","soup of the day",w),true,0). st_obs(informed(w,"they had just run out of the soup","Fiona"),true,1). st_obs(available("soup of the day",r),false,1). st_hpd(order("Fiona","sandwich",w),true,2).
```

### Ground Truth
```clingo
restaurant(r). customer("Fiona"). food("soup of the day"). food("sandwich"). waiter("the waiter"). story_step(0..2). st_hpd(order("Fiona", "soup of the day", "the waiter"), true, 0). st_obs(available("soup of the day", r), false, 1). st_hpd(order("Fiona", "sandwich", "the waiter"), true, 2).
```

---

## Story #59 — Partial Match (Similarity: 0.3077)

**Story:** Lucy visited the health food restaurant. She ordered a kale salad and detox juice. The ingredients were fresh and organic. She felt energized after her meal.

### Predicted
```clingo
customer("Lucy"). person("Lucy"). waiter(w). restaurant("health food restaurant"). food("kale salad"). beverage("detox juice"). st_hpd(enter("Lucy","health food restaurant"),true,0). st_hpd(order("Lucy","kale salad",w),true,1). st_hpd(order("Lucy","detox juice",w),true,1).
```

### Ground Truth
```clingo
restaurant("health food restaurant"). customer("Lucy"). food("kale salad"). beverage("detox juice"). story_step(0..2). st_hpd(enter("Lucy", "health food restaurant"), true, 0). st_hpd(order("Lucy", "kale salad", "the waiter"), true, 1). st_hpd(order("Lucy", "detox juice", "the waiter"), true, 1). st_hpd(eat("Lucy", "kale salad"), true, 2). st_hpd(drink("Lucy", "detox juice"), true, 2).
```

---

## Story #35 — Partial Match (Similarity: 0.3333)

**Story:** One day, Andy felt hungry and went to the RRGrill restaurant for dinner. The restaurant was open, but there was no table available for Andy. Andy decided to leave.

### Predicted
```clingo
person("Andy"). customer("Andy"). restaurant("RRGrill"). st_obs(hungry("Andy"), true, 0). st_hpd(enter("Andy", "RRGrill"), true, 1). st_obs(open("RRGrill"), true, 2). st_hpd(leave("Andy"), true, 3).
```

### Ground Truth
```clingo
restaurant("RRGrill"). customer("Andy"). story_step(0..3). st_hpd(enter("Andy", "RRGrill"), true, 0). st_hpd(lead_to(w, "Andy", t), false). stop_activity("Andy", 2). st_hpd(leave("Andy"), true, 3).
```

---

## Story #46 — Partial Match (Similarity: 0.3333)

**Story:** Rita finished her salad. She requested the bill from the waiter. The waiter brought the bill, and Rita paid with her credit card.

### Predicted
```clingo
customer("Rita"). person("Rita"). waiter(w). food("salad"). st_hpd(eat("Rita", "salad"), true, 0). st_hpd(request("Rita", b, w), true, 1). st_obs(bill_generated("Rita", b), true, 2). st_hpd(pay("Rita", b), true, 3). st_obs(paid(b), true, 3).
```

### Ground Truth
```clingo
restaurant(r). customer("Rita"). food("salad"). waiter("the waiter"). story_step(0..3). st_hpd(eat("Rita", "salad"), true, 0). st_hpd(request("Rita", b, "the waiter"), true, 1). st_hpd(put_down("the waiter", b, t), true, 2). st_hpd(pay("Rita", b), true, 3).
```

---

## Story #41 — Partial Match (Similarity: 0.3529)

**Story:** Laura was at a cafe. She ordered a coffee and a croissant. The waiter brought the coffee promptly, but after 30 minutes, the croissant still hadn't arrived. Laura gave up, paid for her coffee, and left.

### Predicted
```clingo
customer("Laura"). person("Laura"). restaurant("cafe"). waiter(w). beverage("coffee"). food("croissant"). st_obs(in("Laura", "cafe"), true, 0). st_hpd(order("Laura", "coffee", w), true, 1). st_hpd(order("Laura", "croissant", w), true, 1). st_obs(holding("Laura", "coffee"), true, 2). st_hpd(pay("Laura", b), true, 3). st_obs(paid(b), true, 3). st_hpd(leave("Laura"), true, 4).
```

### Ground Truth
```clingo
restaurant("cafe"). customer("Laura"). beverage("coffee"). food("croissant").  waiter("the waiter"). story_step(0..4). st_hpd(order("Laura", "coffee", "the waiter"), true, 0). st_hpd(order("Laura", "croissant", "the waiter"), true, 0). st_hpd(put_down("the waiter", "coffee", t), true, 1). st_obs(served("Laura"), false, 2). st_hpd(pay("Laura", b), true, 3). st_hpd(leave("Laura"), true, 4).
```

---

## Story #85 — Partial Match (Similarity: 0.3636)

**Story:** [REDACTED — original ROCStories text; storyid=9915e783-6bf9-4d92-9150-b031bf778bb7]

### Predicted
```clingo
person("I") restaurant("a restaurant") waiter(w) food("pizza") st_hpd(enter("I", "a restaurant"), true, 0) st_hpd(order("I", "pizza", w), true, 1) st_hpd(request("I", "return the pizza", w), true, 2)
```

### Ground Truth
```clingo
restaurant("a restaurant"). customer("I"). food("pizza"). food("burnt pizza"). st_hpd(enter("I", r), true, 0). st_hpd(order("I", "pizza", w), true, 1). st_hpd(put_down(w, "burnt pizza", t), true, 2). st_hpd(request("I", pick_up(w, "burnt pizza", t), w), true, 3).
```

---

## Story #92 — Partial Match (Similarity: 0.3636)

**Story:** [REDACTED — original ROCStories text; storyid=c9e533e3-d8cc-4e9c-a7a0-0369d6cdc537]

### Predicted
```clingo
customer("I"). restaurant("new restaurant that opened in the mall"). waiter(w). food("large salad"). st_obs(in("I", "new restaurant that opened in the mall"), true, 0). st_hpd(order("I", "large salad", w), true, 1). st_obs(open("new restaurant that opened in the mall"), false, 2).
```

### Ground Truth
```clingo
restaurant("new restaurant"). customer("I"). food("large salad"). food("small salad"). waiter(w). st_obs(in("I", "new restaurant"), true, 0). st_hpd(order("I", "large salad", w), true, 1). st_hpd(put_down(w, "small salad", t), true, 2).
```

---

## Story #99 — Partial Match (Similarity: 0.3636)

**Story:** [REDACTED — original ROCStories text; storyid=11cd400e-b2b8-4279-9e2e-925de49fee44]

### Predicted
```clingo
customer("the family"). restaurant("a new restaurant"). food("tacos"). food("chicken tacos"). food("food"). st_hpd(enter("the family", "a new restaurant"), true, 0). st_obs(available("tacos", "a new restaurant"), true, 1). st_hpd(eat("the family", "food"), true, 2).
```

### Ground Truth
```clingo
restaurant("new restaurant"). customer("The family"). food("different foods"). food("tacos"). st_hpd(enter("The family", "new restaurant"), true, 0). st_hpd(order("The family", "different foods", w), true, 1). st_hpd(eat("The family", "different foods"), true, 2).
```

---

## Story #86 — Partial Match (Similarity: 0.3684)

**Story:** [REDACTED — original ROCStories text; storyid=541efb12-b331-4525-afe1-5422ff33a1ca]

### Predicted
```clingo
person("Samuel") person("John") restaurant("a diner") waiter(w) food("hamburger without onions") food("hotdog") st_obs(in("Samuel", "a diner"), true, 0) st_obs(in("John", "a diner"), true, 0) st_hpd(order("Samuel", "hamburger without onions", w), true, 1) st_obs(served("Samuel"), true, 2) st_hpd(complain("Samuel", w), true, 3) st_next(2, 3) st_obs(served("Samuel"), true, 4)
```

### Ground Truth
```clingo
restaurant("diner"). customer("Samuel"). customer("John"). food("hamburger without onions"). food("hotdog"). waiter("the waiter"). st_obs(in("Samuel", "diner"), true, 0). st_obs(in("John", "diner"), true, 0). st_hpd(order("Samuel", "hamburger without onions", "the waiter"), true, 1). st_hpd(put_down("the waiter", "hotdog", t), true, 2). st_hpd(complain("Samuel", "the waiter"), true, 3). st_next(2,3). st_hpd(put_down("the waiter", "hamburger without onions", t), true, 4).
```

---

## Story #69 — Partial Match (Similarity: 0.3750)

**Story:** A group of coworkers went to a sandwich shop for lunch. The waiter seated them at a long table, and took their orders. The waiter brought out all the sandwiches. They ate, paid their separate bills, and returned to work.

### Predicted
```clingo
restaurant("sandwich shop"). waiter(w). customer("group of coworkers"). food("sandwiches"). st_hpd(enter("group of coworkers", "sandwich shop"), true, 0). st_hpd(lead_to(w, "group of coworkers", t), true, 1). st_obs(at_l(t, "long table"), true, 1). st_hpd(order("group of coworkers", f, w), true, 2). st_obs(at_l("sandwiches", t), true, 3). st_hpd(eat("group of coworkers", "sandwiches"), true, 4). st_hpd(pay("group of coworkers", b), true, 5).
```

### Ground Truth
```clingo
restaurant("sandwich shop"). customer("group of coworkers"). food("sandwiches"). waiter("the waiter"). st_hpd(enter("group of coworkers", "sandwich shop"), true, 0). st_hpd(lead_to("the waiter", "group of coworkers", t), true, 1). st_hpd(order("group of coworkers", "sandwiches", "the waiter"), true, 2). st_hpd(put_down("the waiter", "sandwiches", t), true, 3). st_hpd(eat("group of coworkers", "sandwiches"), true, 4). st_hpd(pay("group of coworkers", b), true, 5). st_hpd(leave("group of coworkers"), true, 6).
```

---

## Story #61 — Partial Match (Similarity: 0.3846)

**Story:** The book club members met at the quiet cafe. They ordered various teas and pastries. Everyone enjoyed their selections while discussing the latest novel.

### Predicted
```clingo
customer("book club members"). restaurant("quiet cafe"). waiter(w). beverage("teas"). food("pastries"). st_hpd(order("book club members", "teas", w), true, 0). st_hpd(order("book club members", "pastries", w), true, 1). st_hpd(drink("book club members", "teas"), true, 2). st_hpd(eat("book club members", "pastries"), true, 3).
```

### Ground Truth
```clingo
restaurant("quiet cafe"). customer("book club members"). food("pastries"). beverage("teas"). story_step(0..2). st_hpd(enter("book club members", "quiet cafe"), true, 0). st_hpd(order("book club members", "pastries", "the waiter"), true, 1). st_hpd(order("book club members", "teas", "the waiter"), true, 1). st_hpd(eat("book club members", "pastries"), true, 2). st_hpd(drink("book club members", "teas"), true, 2).
```

---

## Story #71 — Partial Match (Similarity: 0.3889)

**Story:** Michael entered the bistro and was led to a table by a waitress. He ordered the daily special and a glass of water. The waitress brought his meal promptly. Michael enjoyed his food and asked for the check.

### Predicted
```clingo
restaurant("bistro"). customer("Michael"). person("Michael"). waiter("the waitress"). food("daily special"). beverage("glass of water"). st_hpd(enter("Michael", "bistro"), true, 0). st_hpd(lead_to("the waitress", "Michael", t), true, 1). st_hpd(order("Michael", "daily special", "the waitress"), true, 2). st_hpd(order("Michael", "glass of water", "the waitress"), true, 3). st_obs(served("Michael"), true, 4). st_hpd(request("Michael", b, "the waitress"), true, 5).
```

### Ground Truth
```clingo
restaurant("the bistro"). customer("Michael"). food("daily special"). beverage("water"). waiter("the waitress"). st_hpd(enter("Michael", "the bistro"), true, 0). st_hpd(lead_to("the host", "Michael", t), true, 1). st_hpd(order("Michael", "daily special", "the waitress"), true, 2). st_hpd(order("Michael", "water", "the waitress"), true, 2). st_hpd(put_down("the waitress", "daily special", t), true, 3). st_hpd(put_down("the waitress", "water", t), true, 3). st_hpd(eat("Michael", "daily special"), true, 4). st_hpd(drink("Michael", "water"), true, 4). st_hpd(request("Michael", b, "the waitress"), true, 5).
```

---

## Story #70 — Partial Match (Similarity: 0.4118)

**Story:** The Jackson family went to a pizzeria on Friday night. The waiter led them to a booth. They ordered a large pepperoni pizza and a pitcher of soda. The waiter brought their order to the table. They all loved the pizza.

### Predicted
```clingo
restaurant("pizzeria"). customer("The Jackson family"). person("The Jackson family"). waiter("the waiter"). food("large pepperoni pizza"). beverage("pitcher of soda"). member("large pepperoni pizza", f). member("pitcher of soda", f). st_hpd(enter("The Jackson family", "pizzeria"), true, 0). st_hpd(lead_to("the waiter", "The Jackson family", "booth"), true, 1). st_hpd(order("The Jackson family", "large pepperoni pizza", "the waiter"), true, 2). st_hpd(order("The Jackson family", "pitcher of soda", "the waiter"), true, 3). st_obs(served("The Jackson family"), true, 4).
```

### Ground Truth
```clingo
restaurant("pizzeria"). customer("The Jackson family"). food("large pepperoni pizza"). beverage("pitcher of soda"). waiter("the waiter"). st_hpd(enter("The Jackson family", "pizzeria"), true, 0). st_hpd(lead_to("the waiter", "The Jackson family", t), true, 1). st_hpd(order("The Jackson family", "large pepperoni pizza", "the waiter"), true, 2). st_hpd(order("The Jackson family", "pitcher of soda", "the waiter"), true, 2). st_hpd(put_down("the waiter", "large pepperoni pizza", t), true, 3). st_hpd(put_down("the waiter", "pitcher of soda", t), true, 3). st_hpd(eat("The Jackson family", "large pepperoni pizza"), true, 4).
```

---

## Story #10 — Partial Match (Similarity: 0.4167)

**Story:** Jim is seated at his table in the restaurant. He orders an appetizer. After waiting for 20 minutes and not receiving his food, he decides to leave the restaurant.

### Predicted
```clingo
person("Jim"). customer("Jim"). restaurant(r). waiter(w). food("appetizer"). st_obs(in("Jim", r), true, 0). st_obs(at_l("Jim", t), true, 0). st_obs(sitting("Jim"), true, 0). st_hpd(order("Jim", "appetizer", w), true, 1). st_obs(served("Jim"), false, 2). st_hpd(leave("Jim"), true, 3).
```

### Ground Truth
```clingo
restaurant("the restaurant"). customer("Jim"). food("appetizer"). story_step(0..3). st_obs(sitting("Jim"), true, 0). st_hpd(order("Jim", "appetizer", w), true, 1). st_obs(served("Pete"), false, 2). st_hpd(leave("Jim"), true, 3).
```

---

## Story #63 — Partial Match (Similarity: 0.4615)

**Story:** At a cafe, Ivan ordered an espresso. The waiter brought it to his table. Ivan drank the espresso, left cash on the table for the bill, and then departed.

### Predicted
```clingo
restaurant("cafe"). waiter(w). person("Ivan"). customer("Ivan"). beverage("espresso"). st_hpd(order("Ivan", "espresso", w), true, 0). st_obs(at_l("espresso", t), true, 1). st_obs(served("Ivan"), true, 1). st_hpd(drink("Ivan", "espresso"), true, 2). st_hpd(pay("Ivan", b), true, 3). st_hpd(leave("Ivan"), true, 4).
```

### Ground Truth
```clingo
restaurant("cafe"). customer("Ivan"). beverage("espresso"). waiter("the waiter"). story_step(0..4). st_hpd(order("Ivan", "espresso", "the waiter"), true, 0). st_hpd(put_down("the waiter", "espresso", t), true, 1). st_hpd(drink("Ivan", "espresso"), true, 2). st_hpd(pay("Ivan", b), true, 3). st_hpd(leave("Ivan"), true, 4).
```

---

## Story #72 — Partial Match (Similarity: 0.4667)

**Story:** Susan visited the pancake house for breakfast. She ordered blueberry pancakes and orange juice. The server brought her order quickly. Susan ate her breakfast and paid with her credit card.

### Predicted
```clingo
restaurant("pancake house"). customer("Susan"). person("Susan"). waiter("the server"). food("blueberry pancakes"). beverage("orange juice"). st_hpd(enter("Susan", "pancake house"), true, 0). st_hpd(order("Susan", "blueberry pancakes", "the server"), true, 1). st_hpd(order("Susan", "orange juice", "the server"), true, 2). st_obs(served("Susan"), true, 3). st_hpd(eat("Susan", "blueberry pancakes"), true, 4). st_hpd(pay("Susan", b), true, 5).
```

### Ground Truth
```clingo
restaurant("the pancake house"). customer("Susan"). food("blueberry pancakes"). beverage("orange juice"). waiter("the server"). st_hpd(enter("Susan", "the pancake house"), true, 0). st_hpd(order("Susan", "blueberry pancakes", "the server"), true, 1). st_hpd(order("Susan", "orange juice", "the server"), true, 1). st_hpd(put_down("the server", "blueberry pancakes", t), true, 2). st_hpd(eat("Susan", "blueberry pancakes"), true, 3). st_hpd(pay("Susan", b), true, 4).
```

---

## Story #96 — Partial Match (Similarity: 0.5000)

**Story:** [REDACTED — original ROCStories text; storyid=77710d2a-dbc2-4c99-a892-190b529ad219]

### Predicted
```clingo
customer("Dina"). person("a friend"). restaurant("fast food restaurant"). waiter(w). food("fries"). member("Dina", "Dina and a friend"). member("a friend", "Dina and a friend"). member("fries", f). st_obs(in("Dina", "fast food restaurant"), true, 0). st_obs(hungry("Dina"), false, 1). st_hpd(order("Dina and a friend", f, w), true, 2). st_hpd(pay("Dina", b), true, 3). st_hpd(pay("a friend", b), true, 3). st_hpd(eat("Dina", "fries"), true, 4).
```

### Ground Truth
```clingo
restaurant("fast food restaurant"). customer(they). person("Dina"). person("a friend"). member("Dina", they). member("a friend", they). food("fries"). st_obs(in("Dina", "fast food restaurant"), true, 0). st_obs(hungry("Dina"), false, 1). st_hpd(order(they, "fries", w), true, 2). st_hpd(pay("Dina", b), true, 3). st_hpd(pay("a friend", b), true, 3). st_hpd(eat("Dina", "fries"), true, 4).
```

---

## Story #98 — Partial Match (Similarity: 0.6000)

**Story:** [REDACTED — original ROCStories text; storyid=09a69527-2433-4e12-9943-9dcacbdf9b04]

### Predicted
```clingo
customer("Joe"). restaurant("the new place"). waiter(w). food("meal"). st_obs(hungry("Joe"), true, 0). st_hpd(enter("Joe", "the new place"), true, 1). st_hpd(order("Joe", "meal", w), true, 2). st_obs(hungry("Joe"), false, 3).
```

### Ground Truth
```clingo
restaurant("new place"). customer("Joe"). food("a meal"). st_obs(hungry("Joe"), true, 0). st_hpd(enter("Joe", "new place"), true, 1). st_hpd(order("Joe", "a meal", w), true, 2). st_hpd(eat("Joe", "a meal"), true, 3). st_obs(hungry("Joe"), false, 4).
```

---

## Story #68 — Partial Match (Similarity: 0.6667)

**Story:** Frank sat down at his usual table in the local diner. The waitress brought him a black coffee. Frank looked at the menu and then ordered pancakes. He ate them, left cash on the table for the bill, and left.

### Predicted
```clingo
restaurant("local diner"). waiter("the waitress"). person("Frank"). customer("Frank"). beverage("black coffee"). food("pancakes"). st_hpd(sit("Frank"), true, 0). st_obs(sitting("Frank"), true, 1). st_obs(at_l("black coffee", t), true, 1). st_hpd(read_menu("Frank"), true, 2). st_hpd(order("Frank", "pancakes", "the waitress"), true, 3). st_hpd(eat("Frank", "pancakes"), true, 4). st_hpd(pay("Frank", b), true, 5). st_hpd(leave("Frank"), true, 6).
```

### Ground Truth
```clingo
restaurant("local diner"). customer("Frank"). beverage("black coffee"). food("pancakes"). waiter("the waitress"). story_step(0..6). st_obs(sitting("Frank"), true, 0). st_hpd(put_down("the waitress", "black coffee", t), true, 1). st_hpd(read_menu("Frank"), true, 2). st_hpd(order("Frank", "pancakes", "the waitress"), true, 3). st_hpd(eat("Frank", "pancakes"), true, 4). st_hpd(pay("Frank", b), true, 5). st_hpd(leave("Frank"), true, 6).
```

---
