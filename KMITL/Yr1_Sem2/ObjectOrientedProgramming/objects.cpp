#include "objects.hpp"
#include <cmath>

const int MAX_BULLETS = 100;

// player class

Player::Player() {
    health = 100;
    score = 0;
    lives = 3;
    playerTexture.loadFromFile("images/player.png");
    spriteplayer.setTexture(playerTexture);
    hitbox.loadFromFile("images/redsquare.png");
    hitboxsprite.setTexture(hitbox);
    hitboxsprite.setScale(0.01, 0.01);
    bulletTexture.loadFromFile("images/bullet.png");
    x = 400;
    y = 500;
    bulletManager = new BulletManager(bulletTexture);
}

void Player::shoot()
{
    if (bulletCooldown <= 0)
    {
        bulletCooldown = 10;
        bulletManager->GetNextAvailableBullet()->setBullet(x, y, 25, 0, 0);
    }
    else
    {
        bulletCooldown--;
    }
}

void Player::draw(sf::RenderWindow &window)
{

    spriteplayer.setPosition(x, y);
    hitboxsprite.setPosition(x+9, y+16);
    window.draw(spriteplayer);
    window.draw(hitboxsprite);

    bulletManager->DrawBullets(window);
}

void Player::update(double player_velocity)
{
    if (1 == sf::Keyboard::isKeyPressed(sf::Keyboard::Left) && x > 0)
    {
        x -= player_velocity;
    }
    if (1 == sf::Keyboard::isKeyPressed(sf::Keyboard::Right) && x < 755)
    {
        x += player_velocity;
    }
    if (1 == sf::Keyboard::isKeyPressed(sf::Keyboard::Up) && y > 0)
    {
        y -= player_velocity;
    }
    if (1 == sf::Keyboard::isKeyPressed(sf::Keyboard::Down) && y < 540)
    {
        y += player_velocity;
    }

    //shooting and managing the bullets
    if (1 == sf::Keyboard::isKeyPressed(sf::Keyboard::Space))
    {
        shoot();
    }

    bulletManager->UpdateBullets();
}


// Enemy classes

Enemy::Enemy(){
    x = 0;
    y = 0;
}

Enemy::Enemy(double x, double y){
    this->x = x;
    this->y = y;
}

Enemy::~Enemy(){}

void Enemy::draw(sf::RenderWindow &window)
{
    spriteenemy.setPosition(x, y);
    window.draw(spriteenemy);
}

void Enemy::update(double enemy_velocity)
{
    y += enemy_velocity;
}

Red_Enemy::Red_Enemy(double x, double y): Enemy(x, y){
    health = 3;
    score = 100;
    enemyTexture.loadFromFile("images/redfairy.png");
    spriteenemy.setTexture(enemyTexture);

}

Red_Enemy::~Red_Enemy(){
}

Black_Enemy::Black_Enemy(double x, double y): Enemy(x, y){
    health = 5;
    score = 200;
    enemyTexture.loadFromFile("images/blackfairy.png");
    spriteenemy.setTexture(enemyTexture);
}

Black_Enemy::~Black_Enemy(){
}

Purple_Enemy::Purple_Enemy(double x, double y): Enemy(x, y){
    health = 10;
    score = 500;
    enemyTexture.loadFromFile("images/purplefairy.png");
    spriteenemy.setTexture(enemyTexture);
}

Purple_Enemy::~Purple_Enemy(){}


// Bullet classes

Bullet::Bullet(double x, double y, double velocity, double angle, double radius, sf::Texture bulletTexture){
    this->x = x;
    this->y = y;
    this->velocity = velocity;
    this->angle = angle;
    this->radius = radius;    
    this->bulletTexture = bulletTexture;
    spritebullet.setTexture(this->bulletTexture);
    sf::Color spriteColor = spritebullet.getColor();
    spriteColor.a = 192; // Set alpha to 192 (75% opacity)
    spritebullet.setColor(spriteColor);
}

Bullet::~Bullet(){}

void Bullet::update(){
    x += std::cos(angle) * velocity;
    y += std::sin(angle) * velocity;
}

void Bullet::draw(sf::RenderWindow &window){
    spritebullet.setPosition(round(x), round(y));
    window.draw(spritebullet);
}

bool Bullet::IsOffScreen() {
    if (x < 0 || x > 800 || y < 0 || y > 600) {
        return true;
    }
    return false;
}

void Bullet::setBullet(double x, double y, double velocity, double angle, double radius){
    this->x = x;
    this->y = y;
    this->velocity = velocity;
    this->angle = angle;
    this->radius = radius;
}

PlayerBullet::PlayerBullet(double x, double y, double velocity, double angle, double radius, sf::Texture bulletTexture) : Bullet(x, y, velocity, angle, radius, bulletTexture){
    acceleration = 0;
    state = 1;
}

PlayerBullet::~PlayerBullet(){}

void PlayerBullet::update(){
    switch(state){
        case 1:
            y -= velocity;
            break;
        case 2:
            x += std::cos(angle) * velocity;
            y += std::sin(angle) * velocity;
            break;
        case 3:
            break;
    }

}


//Bullet Manager

BulletManager::BulletManager() {
    bulletVector.resize(MAX_BULLETS); // Resize the vector
    active.resize(MAX_BULLETS); // Resize the vector

    for (int i = 0; i < MAX_BULLETS; ++i) {
        bulletVector[i] = new PlayerBullet(900, 900, 0, 0, 0, sf::Texture());
        active[i] = false;
    }
}

BulletManager::BulletManager(sf::Texture bulletTexture) {
    bulletVector.resize(MAX_BULLETS); // Resize the vector
    active.resize(MAX_BULLETS); // Resize the vector

    for (int i = 0; i < MAX_BULLETS; ++i) {
        bulletVector[i] = new PlayerBullet(900, 900, 0, 0, 0, bulletTexture);
        active[i] = false;
    }
}

BulletManager::~BulletManager() {
    for (int i = 0; i < MAX_BULLETS; ++i) {
        delete bulletVector[i];
    }
}

BulletManager& BulletManager::operator=(const BulletManager& other) {
    if (this == &other) {
        return *this; // Self-assignment check
    }

    // Perform the assignment of member variables
    bulletVector.clear();
    bulletVector.reserve(other.bulletVector.size());
    for (const auto* bullet : other.bulletVector) {
        bulletVector.push_back(new Bullet(*bullet));
    }

    active = other.active;
    bulletTexture = other.bulletTexture;

    return *this;
}

Bullet* BulletManager::GetNextAvailableBullet() {
    for (int i = 0; i < MAX_BULLETS; ++i) {
        if (!active[i]) {
            active[i] = true;
            return bulletVector[i];
        }
    }
    bulletVector.push_back(new PlayerBullet(900, 900, 0, 0, 0, bulletTexture));
    active.push_back(false);
    return bulletVector[bulletVector.size() - 1];
}

void BulletManager::UpdateBullets() {
    for (int i = 0; i < bulletVector.size(); ++i) {
        if (active[i]) {
            bulletVector[i]->update();
            if (bulletVector[i]->IsOffScreen()) {
                active[i] = false;
            }
        }
    }
}

void BulletManager::DrawBullets(sf::RenderWindow &window) {
    for (int i = 0; i < bulletVector.size(); ++i) {
        if (active[i]) {
            bulletVector[i]->draw(window);
        }
    }
}