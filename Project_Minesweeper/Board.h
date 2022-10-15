#include <SFML/Graphics.hpp>
#include <fstream>
#include <vector>
#include <map>
#include <iostream>
#include <ctime>
#include "Tile.h"
using namespace std;
using namespace sf;

class Board{
    public:
        int width;
        int height;
        Board();
        void update(RenderWindow &window);
        void initTexture();
        void genTiles();
        void randBits();
        void printNbrs();
        void tileNbrs();
        void resetTiles();
        void testBoard(string option);
        int getTile(int x,int y);
        void setCounter();
        void setFace();
        void draw(RenderWindow &window);
    private:
        map<string,Texture> imgAssets;
        vector<Tile> boardTiles;
        vector<int> tileBits;
        Sprite test1;
        Sprite test2;
        Sprite test3;
        Sprite d1;
        Sprite d2;
        Sprite d3;
        Sprite d4;
        Sprite face;
        Sprite debug;
        bool gameLost;
        bool gameWon;
        int numMines;
        int numFlags;
        int counter;
        int numTiles;
};

Board::Board(){
    ifstream ifs;
    gameLost = false;
    gameWon = false;
    
    ifs.open("./boards/config.cfg");
    ifs>>width;
    ifs>>height;
    ifs>>numMines;
    ifs.close();

    numFlags = 0;
    counter = numMines-numFlags;
    numTiles = (width*height) - numMines;



    initTexture();

    test1.setTexture(imgAssets["test_1"]);
    test2.setTexture(imgAssets["test_2"]);
    test3.setTexture(imgAssets["test_3"]);
    d1.setTexture(imgAssets["digits"]);
    d2.setTexture(imgAssets["digits"]);
    d3.setTexture(imgAssets["digits"]);
    d4.setTexture(imgAssets["digits"]);
    face.setTexture(imgAssets["face_happy"]);
    debug.setTexture(imgAssets["debug"]);

    int ones = numMines % 10;
    int tens = (numMines / 10) % 10;
    int hundreds = numMines /100;


    d1.setTextureRect(IntRect(21*ones,0,21,32));
    d2.setTextureRect(IntRect(21*tens,0,21,32));
    d3.setTextureRect(IntRect(21*hundreds,0,21,32));
    d4.setTextureRect(IntRect(0,0,21,32));

    d4.setPosition(0,32*height);
    d3.setPosition(21,32*height);
    d2.setPosition(42,32*height);
    d1.setPosition(63,32*height);
    face.setPosition((width*32-64)/2,32*height);
    debug.setPosition(32*width-64*4,32*height);
    test1.setPosition(32*width-64*3,32*height);
    test2.setPosition(32*width-64*2,32*height);
    test3.setPosition(32*width-64,32*height);

    genTiles();
    randBits();
    resetTiles();
}

void Board::update(RenderWindow &window){
    Vector2i pos;
    if(Mouse::isButtonPressed(Mouse::Left)){
        pos = Mouse::getPosition(window);
        if((pos.x>=0 && pos.x<=width*32) && (pos.y>=0 && pos.y<=32*height) && !(gameLost||gameWon) && !boardTiles[getTile(pos.x,pos.y)].flagged){
            boardTiles[getTile(pos.x,pos.y)].reveal(numTiles);
            if(numTiles==0){
                gameWon = true;
            }
            if(boardTiles[getTile(pos.x,pos.y)].isMine){
                gameLost = true;
                for(int i=0; i<height*width; i++){
                    if(boardTiles[i].isMine){
                        boardTiles[i].reveal(numTiles);
                    }
                }
            }
        }
        else if(pos.y>32*height && pos.y<=32*height+64){
            if(pos.x >= (width*32-64)/2 && pos.x <= (width*32-64)/2 + 64){
                randBits();
                resetTiles();
                setCounter();
            }
            else if(pos.x>=32*width-64*4 && pos.x<32*width-64*3 && !(gameWon||gameLost)){
                for(int i=0; i<height*width; i++){
                    boardTiles[i].dbg();
                }
            }
            else if(pos.x>=32*width-64*3 && pos.x<32*width-64*2){
                testBoard("./boards/testboard1.brd");
                resetTiles();
                setCounter();
            }
            else if(pos.x>=32*width-64*2 && pos.x<32*width-64){
                testBoard("./boards/testboard2.brd");
                resetTiles();
                setCounter();
            }
            else if(pos.x>=32*width-64 && pos.x<32*width){
                testBoard("./boards/testboard3.brd");
                resetTiles();
                setCounter();
            }
        }   
    }
    else if(Mouse::isButtonPressed(Mouse::Right) && !(gameLost||gameWon)){
        pos = Mouse::getPosition(window);
        if((pos.x>=0 && pos.x<=width*32) && (pos.y>=0 && pos.y<=32*height) && !(gameLost||gameWon)){
            if(boardTiles[getTile(pos.x,pos.y)].flagged && !boardTiles[getTile(pos.x,pos.y)].debugMode){
                numFlags--;
                boardTiles[getTile(pos.x,pos.y)].handleFlag();
            }
            else if(!boardTiles[getTile(pos.x,pos.y)].revealed && !boardTiles[getTile(pos.x,pos.y)].debugMode){
                numFlags++;
                boardTiles[getTile(pos.x,pos.y)].handleFlag();
            }
            setCounter();
        }
    }
    setFace();
    draw(window);
}

void Board::initTexture(){
    vector<string> names = {"debug","digits","face_happy","face_lose","face_win","flag","mine","number_1","number_2","number_3","number_4","number_5","number_6","number_7","number_8","test_1","test_2","test_3","tile_hidden","tile_revealed"};
    Texture t;
    String s;
    for(int i=0; i<names.size(); i++){
        s = "./images/" + names.at(i) + ".png";
        t.loadFromFile(s);
        imgAssets.emplace(names.at(i),t);
    }
}

void Board::genTiles(){
    for(int i = 0; i<height; i++){
        for(int j=0; j<width; j++){
            Tile t = Tile(imgAssets["tile_revealed"],imgAssets["tile_hidden"],imgAssets["flag"],(float)(32*j),(float)(32*i));
            t.index = "(" + to_string(j) + "," + to_string(i) + ")";
            boardTiles.push_back(t);
        }
    }
}

void Board::randBits(){
    srand(time(NULL));
    tileBits.clear();
    ifstream ifs;
    ifs.open("./boards/config.cfg");
    ifs>>width;
    ifs>>height;
    ifs>>numMines;
    ifs.close();

    int x;
    map<int,int> r; 
    for(int i=0; i<height*width; i++){
        tileBits.push_back(0);
    }

    while(r.size() < numMines){
        x = rand() % (height*width);
        r.emplace(x,x);
    }

    for(int j =0; j<height*width; j++){
        if(r.count(j)){
            tileBits[j] = 1;
        }
    }
}

void Board::printNbrs(){
    for(int j=0; j<width*height; j++){
        cout<<"Tile: "<<j<<", ";
        for(int i=0; i<boardTiles[j].nbrs.size(); i++){
            cout<<boardTiles[j].nbrs[i]->index<<" ";
        }
        cout<<endl;
    }
}

void Board::tileNbrs(){
    for(int i = 0; i<height*width; i++){
        boardTiles[i].nbrs.clear();
        if(i == 0 || i == width-1 || i==width*(height-1) || i==width*height-1){
            for(int a=0; a<3; a++){
                boardTiles[i].nbrs.push_back(nullptr);
            }
            if(i==0){
                boardTiles[i].nbrs[0] = &boardTiles[i + 1];
                boardTiles[i].nbrs[1] = &boardTiles[i + width];
                boardTiles[i].nbrs[2] = &boardTiles[i + width+1];
            }
            else if(i==width-1){
                boardTiles[i].nbrs[0] = &boardTiles[i - 1];
                boardTiles[i].nbrs[1] = &boardTiles[i + width-1];
                boardTiles[i].nbrs[2] = &boardTiles[i + width];
            }
            else if(i==width*(height-1)){
                boardTiles[i].nbrs[0] = &boardTiles[i + 1];
                boardTiles[i].nbrs[1] = &boardTiles[i - width+1];
                boardTiles[i].nbrs[2] = &boardTiles[i - width];
            }
            else{
                boardTiles[i].nbrs[0] = &boardTiles[i - 1];
                boardTiles[i].nbrs[1] = &boardTiles[i - width];
                boardTiles[i].nbrs[2] = &boardTiles[i - width-1];
            }
        }
        else if(i>width*(height-1) || i<width || i%width==0 || i%width==width-1){
            for(int b=0; b<5; b++){
                boardTiles[i].nbrs.push_back(nullptr);
            }
            if(i>width*(height-1)){
                boardTiles[i].nbrs[0] = &boardTiles[i - 1];
                boardTiles[i].nbrs[1] = &boardTiles[i + 1];
                boardTiles[i].nbrs[2] = &boardTiles[i - width+1];
                boardTiles[i].nbrs[3] = &boardTiles[i - width];
                boardTiles[i].nbrs[4] = &boardTiles[i - width-1];
            }
            else if(i%width==0){
                boardTiles[i].nbrs[0] = &boardTiles[i + 1];
                boardTiles[i].nbrs[1] = &boardTiles[i - width+1];
                boardTiles[i].nbrs[2] = &boardTiles[i + width];
                boardTiles[i].nbrs[3] = &boardTiles[i - width];
                boardTiles[i].nbrs[4] = &boardTiles[i + width+1];
            }
            else if(i%width==width-1){
                boardTiles[i].nbrs[0] = &boardTiles[i - 1];
                boardTiles[i].nbrs[1] = &boardTiles[i + width-1];
                boardTiles[i].nbrs[2] = &boardTiles[i - width];
                boardTiles[i].nbrs[3] = &boardTiles[i + width];
                boardTiles[i].nbrs[4] = &boardTiles[i - width - 1];
            }
            else{
                boardTiles[i].nbrs[0] = &boardTiles[i - 1];
                boardTiles[i].nbrs[1] = &boardTiles[i + 1];
                boardTiles[i].nbrs[2] = &boardTiles[i + width -1];
                boardTiles[i].nbrs[3] = &boardTiles[i + width];
                boardTiles[i].nbrs[4] = &boardTiles[i + width+1];
            }
        }
        else{
            for(int c=0; c<8; c++){
                boardTiles[i].nbrs.push_back(nullptr);
            }
            boardTiles[i].nbrs[0] = &boardTiles[i - 1];
			boardTiles[i].nbrs[1] = &boardTiles[i + 1];
			boardTiles[i].nbrs[2] = &boardTiles[i + width-1];
			boardTiles[i].nbrs[3] = &boardTiles[i - width+1];
			boardTiles[i].nbrs[4] = &boardTiles[i + width];
			boardTiles[i].nbrs[5] = &boardTiles[i - width];
			boardTiles[i].nbrs[6] = &boardTiles[i + width+1];
			boardTiles[i].nbrs[7] = &boardTiles[i - width-1];
        }
    }
}

void Board::testBoard(string file){
    ifstream ifs;
    ifs.open(file);
    tileBits.clear();
    string bits;
    int c1 = 0;
    int c2 = 0;
    while(getline(ifs,bits)){
        width = bits.length();
        c1++;
        for(char c: bits){
            tileBits.push_back(c-'0');
            if(c == '1'){
                c2++;
            }
        }
    }
    ifs.clear();
    height = c1;
    numMines = c2;
}

void Board::resetTiles(){
    gameLost = false;
    gameWon = false;
    counter = numMines;
    numFlags = 0;
    numTiles = width*height - numMines;


    for(int i=0; i<height*width; i++){
        boardTiles[i].mineCount = 0;
        boardTiles[i].isMine = tileBits[i];
    }


    tileNbrs();

    //printNbrs();

    for(int j=0; j<height*width; j++){
        for(int k=0; k<boardTiles[j].nbrs.size(); k++){
            if(boardTiles[j].nbrs[k]->isMine){
                boardTiles[j].mineCount+=1;
            }
        }

    }
    for(int k=0; k<height*width; k++){
        boardTiles[k].update(imgAssets);
    }
}

int Board::getTile(int x, int y){
    return (y / 32) * width + (x / 32) ;
}

void Board::setCounter(){
    counter = numMines - numFlags;
    int ones;
    int tens;
    int hundreds;
    if(counter>0){
         ones = counter % 10;
         tens = (counter / 10) % 10;
         hundreds = counter /100;

         d1.setTextureRect(IntRect(21*ones,0,21,32));
         d2.setTextureRect(IntRect(21*tens,0,21,32));
         d3.setTextureRect(IntRect(21*hundreds,0,21,32));
    }
    else if(counter == 0){
        d1.setTextureRect(IntRect(0,0,21,32));
        d2.setTextureRect(IntRect(0,0,21,32));
        d3.setTextureRect(IntRect(0,0,21,32));
        d4.setTextureRect(IntRect(0,0,21,32));
    }
    else{
        ones = (counter*-1) % 10;
        tens = ((counter*-1) / 10) % 10;
        hundreds = (counter*-1) /100;

        d1.setTextureRect(IntRect(21*ones,0,21,32));
        d2.setTextureRect(IntRect(21*tens,0,21,32));
        d3.setTextureRect(IntRect(21*hundreds,0,21,32));
        d4.setTextureRect(IntRect(210,0,21,32));
    }
}

void Board::setFace(){
    if(gameLost){
        face.setTexture(imgAssets["face_lose"]);
    }
    else if(gameWon){
        for(int i=0; i<width*height; i++){
            if(boardTiles[i].debugMode){
                boardTiles[i].dbg();
            }
            if(boardTiles[i].isMine && !boardTiles[i].flagged){
                boardTiles[i].handleFlag();
                numFlags++;
            }
        }
        setCounter();
        face.setTexture(imgAssets["face_win"]);
    }
    else{
        face.setTexture(imgAssets["face_happy"]);
    }
}

void Board::draw(RenderWindow &window){
    for(int i=0; i<height*width; i++){
        boardTiles[i].draw(window);
    }
    window.draw(test1);
    window.draw(test2);
    window.draw(test3);
    window.draw(face);
    window.draw(debug);
    window.draw(d1);
    window.draw(d2);
    window.draw(d3);
    window.draw(d4);
}