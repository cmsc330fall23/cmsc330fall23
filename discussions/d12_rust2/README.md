# Discussion 12 - Friday, December 1<sup>st</sup>

## Reminders

- Exam 2 grades & solutions posted: [@2017](https://piazza.com/class/lkimk0rc39wfi/post/2017)
  - Regrades open until **11:59 PM tomorrow, December 2nd**
- Quiz 4 next **Friday, December 8th**

## Resources

- [Rust Book - Defining and Instantiating Structs](https://doc.rust-lang.org/book/ch05-01-defining-structs.html)
- [Rust Book - Defining an Enum](https://doc.rust-lang.org/book/ch06-01-defining-an-enum.html)
- [Rust Book - Traits](https://doc.rust-lang.org/book/ch10-02-traits.html)

## Exercise

Let's try to implement a simplified game of Pokemon: [`main.rs`](./src/main.rs)

Take a couple of minutes to read through the code and understand the different traits, enums, and structures being used.

### Instantiate Pokemon

Let's start by creating some Pokemon to play with. Here are some examples:

```txt
Squirtle (Water):
- 50/50 HP, Level 5
- Moves:
  - Tackle (Normal),   does 10 damage
  - Water Gun (Water), does 15 damage

Charmander (Fire):
- 60/60 HP, Level 6
- Moves:
  - Scratch (Normal),  does 10 damage
  - Ember (Fire),      does 15 damage

Bulbasaur (Grass):
- 40/40 HP, Level 4
- Moves:
  - Tackle (Normal),   does 10 damage
  - Vine Whip (Grass), does 15 damage
```

Rust code for the Charmander from above:

```rust
let mut charmander = PokemonCharacter {
    name: String::from("Charmander"),
    level: 6,
    hp: 60,
    max_hp: 60,
    pokemon_type: PokemonType::Fire,
    moves: vec![
        PokemonMove {
            name: String::from("Scratch"),
            move_type: PokemonType::Normal,
            damage: 10,
        },
        PokemonMove {
            name: String::from("Ember"),
            move_type: PokemonType::Fire,
            damage: 15,
        },
    ],
};
```

### Summary

I want to implement a `Summary` trait for my Pokemon so I can see their current health & level. I should be able to call it like so:

```rust
println!("{}", squirtle.summary());
println!("{}", charmander.summary());
```

An example of what the output could look like:

```bash
[Squirtle]: 93/100 HP, Level 10
[Charmander]: 50/50 HP, Level 5
```

### Battle

Let's simulate a basic pokemon battle. Here's an example battle:

```rust
println!("{}", charmander.summary());
println!("{}", squirtle.summary());
println!();

charmander.attack(&mut squirtle);
squirtle.attack(&mut charmander);
println!();

println!("{}", charmander.summary());
println!("{}", squirtle.summary());
println!();

println!("Leveling up Squirtle, healing charmander...");
println!();

squirtle.level_up();
charmander.heal();

println!("{}", charmander.summary());
println!("{}", squirtle.summary());
println!();
```

Example output:

```txt
[Charmander]: 60/60 HP, Level 6
[Squirtle]: 50/50 HP, Level 5

Charmander used Scratch!
Squirtle took 10 damage!
Squirtle used Water Gun!
It's super effective!
Charmander took 30 damage!

[Charmander]: 30/60 HP, Level 6
[Squirtle]: 40/50 HP, Level 5

Leveling up Squirtle, healing charmander...

[Charmander]: 60/60 HP, Level 6
[Squirtle]: 60/60 HP, Level 6
```
