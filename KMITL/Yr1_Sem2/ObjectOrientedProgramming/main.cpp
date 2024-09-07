#include <SFML/Graphics.hpp>
#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <chrono>
#include "objects.hpp"
#include "objects.cpp"


bool collision(sf::Sprite sprite1, sf::Sprite sprite2)
{
    return sprite1.getGlobalBounds().intersects(sprite2.getGlobalBounds());
}


int main()
{
    


    sf::RenderWindow window(sf::VideoMode(800, 600), "Shmup game!");
    window.setFramerateLimit(60);


    sf::Texture background1Texture;
    sf::Texture background2Texture;

    background1Texture.loadFromFile("images/starfield1.png");
    background2Texture.loadFromFile("images/starfield2.png");

    sf::Sprite background1Sprite(background1Texture);
    sf::Sprite background2Sprite(background2Texture);

    background1Sprite.setPosition(0,0);
    background2Sprite.setPosition(0,-600);


    sf::Texture playerTexture;
    sf::Sprite spriteplayer;

    sf::Event event;


    Player player;
    Player player2;
    double player_velocity = 4;
    double enemy_velocity = 1.5;

    std::vector<Enemy*> enemies;
    

    int level = 1;
    int enemy_count = 0;
    int enemy_per_level = 0;
    int spawn_timer = 0;
    
    srand(time(NULL));


    
    while (1 == window.isOpen())
    {
       


        spawn_timer++;
        sf::Event event;
        while (window.pollEvent(event)){if (event.type == sf::Event::Closed){window.close();}}

        background2Sprite.move(0, 1);
        background1Sprite.move(0, 1);
        if (background1Sprite.getPosition().y >= 600)
            background1Sprite.setPosition(0,-600);
        if (background2Sprite.getPosition().y >= 600)
            background2Sprite.setPosition(0,-600);

        if ((enemy_count < enemy_per_level) && spawn_timer == 200 ){
            spawn_timer = 0;
            int random = rand() % 3;

            if (random == 0){
                enemies.push_back(new Red_Enemy(rand() % 700, -20));
                enemy_count++;
            }
            else if (random == 1){
                enemies.push_back(new Black_Enemy(rand() % 700, -20));
                enemy_count++;
                }
            else if (random == 2){
                enemies.push_back(new Purple_Enemy(rand() % 700, -20));
                enemy_count++;
                }
        }

        if (enemy_count == 0){
            level++;
            enemy_per_level += 5;
        }



        for (int i = 0; i < enemies.size(); i++){
            if (enemies[i]->y > 600 ||enemies[i]->health <= 0 ){
                enemies.erase(enemies.begin() + i);
                }
        }

        
        window.clear();
        
        window.draw(background1Sprite);
        window.draw(background2Sprite);
        player.draw(window);


        //player2.draw(window);
        player.update(player_velocity);


        for (auto v : enemies){
            v->draw(window);
            v->update(enemy_velocity);
        }


        window.display();

    //    std::cout << "x =" << player.x << " y =" << player.y << std::endl;

    //    if(collision(player.hitboxsprite, player2.hitboxsprite))
    //    {
    //        std::cout << "collision" << std::endl;
    //    }
    //    else
    //    {
    //        std::cout << "no collision" << std::endl;
    //    }

    }

    return 0;
}
