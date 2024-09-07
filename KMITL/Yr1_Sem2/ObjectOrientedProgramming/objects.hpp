#ifndef OBJECTS_HPP
#define OBJECTS_HPP

//const int MAX_BULLETS = 100;

#include <iostream>
#include <string>
#include <vector>
#include<array>
#include <SFML/Graphics.hpp>

class Bullet;
class PlayerBullet;
class BulletManager;

class Player{
    private:
        int health;
        int score;
        int lives;
        double x;
        double y;
        double bulletCooldown = 0;

        sf::Texture playerTexture;
        sf::Sprite spriteplayer;
        
        sf::Texture hitbox;
        sf::Sprite hitboxsprite;

        sf::Texture bulletTexture;

        BulletManager* bulletManager;

    public:
        Player();
        void shoot();
        void draw(sf::RenderWindow &window);
        void update(double player_velocity);
        void invincible();

};

class Enemy{
    public:
        int health;
        int score;
        double x;
        double y;

        sf::Texture enemyTexture;
        sf::Sprite spriteenemy;
        
        Enemy();
        Enemy(double x, double y);

        ~Enemy();

        //virtual void shoot();
        void draw(sf::RenderWindow &window);
        void update(double enemy_velocity);

        
};

class Red_Enemy: public Enemy{
    public:
        Red_Enemy(double x, double);
        virtual ~Red_Enemy();
};

class Black_Enemy: public Enemy{
    public:
        Black_Enemy(double x, double y);
        ~Black_Enemy();
};

class Purple_Enemy: public Enemy{
    public:
        Purple_Enemy(double x, double y);
        ~Purple_Enemy();
};

class Bullet{
    protected:
        double x;
        double y;
        double velocity;
        double acceleration;
        double angle; // in rad
        double radius;
        int state;
        sf::Texture bulletTexture;
        sf::Sprite spritebullet;

    public :
        Bullet(double x, double y, double velocity, double angle, double radius, sf::Texture bulletTexture);
        ~Bullet();
        void draw(sf::RenderWindow &window);
        virtual void update();
        bool IsOffScreen();
        void setBullet(double x, double y, double velocity, double angle, double radius);
        //void setBullet(double x, double y, double velocity, double angle, double radius, sf::Texture bulletTexture);
};

class PlayerBullet : public Bullet{
    public:
        PlayerBullet();
        PlayerBullet(double x, double y, double velocity, double angle, double radius, sf::Texture bulletTexture);
        ~PlayerBullet();
        virtual void update() override;
};

class EnemyBullet : public Bullet{
    public:
        EnemyBullet(double x, double y, double velocity, double angle, double radius);
        void update();
};

class BulletManager {
private:
    std::vector<Bullet*> bulletVector;
    std::vector<bool> active;
    sf::Texture bulletTexture;

public:
    BulletManager();
    BulletManager(sf::Texture bulletTexture);
    ~BulletManager();
    BulletManager& operator=(const BulletManager& other);
    Bullet* GetNextAvailableBullet();
    void UpdateBullets();
    void DrawBullets(sf::RenderWindow &window);
};

#endif