use rand::seq::SliceRandom;

#[derive(Clone, Copy)]
enum PokemonType {
    Normal,
    Fire,
    Water,
    Electric,
    Grass,
}

struct PokemonMove {
    name: String,
    move_type: PokemonType,
    damage: u32,
}

struct PokemonCharacter {
    name: String,
    level: u32,
    hp: u32,
    max_hp: u32,
    pokemon_type: PokemonType,
    moves: Vec<PokemonMove>,
}

trait Pokemon {
    fn level_up(&mut self);
    fn heal(&mut self);
    fn attack(&mut self, enemy: &mut PokemonCharacter);
}

static BATTLE_MATRIX: [[f32; 5]; 5] = [
    // Normal, Fire, Water, Electric, Grass
    [1.0, 1.0, 1.0, 1.0, 1.0], // Normal
    [1.0, 0.5, 0.5, 1.0, 2.0], // Fire
    [1.0, 2.0, 0.5, 1.0, 0.5], // Water
    [1.0, 1.0, 2.0, 0.5, 0.5], // Electric
    [1.0, 0.5, 2.0, 1.0, 2.0], // Grass
];

impl Pokemon for PokemonCharacter {
    fn level_up(&mut self) {
        self.level += 1;
        self.max_hp += 10;
        self.heal();
    }

    fn heal(&mut self) {
        self.hp = self.max_hp;
    }

    fn attack(&mut self, enemy: &mut PokemonCharacter) {
        let my_move = self.moves.choose(&mut rand::thread_rng()).unwrap();
        let scalar = BATTLE_MATRIX[my_move.move_type as usize][enemy.pokemon_type as usize];

        println!("{} used {}!", self.name, my_move.name);

        if scalar == 2.0 {
            println!("It's super effective!");
        } else if scalar == 0.5 {
            println!("It's not very effective...");
        }

        let damage_taken = ((my_move.damage as f32) * scalar) as u32;
        enemy.hp -= damage_taken;

        println!("{} took {} damage!", enemy.name, damage_taken);
    }
}

// TODO: create & implement Summary trait for PokemonCharacter

fn main() {
    // TODO: instantiate pokemon, call summary(), use battle functions
}
