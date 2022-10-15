#include <fstream>
#include <iostream>
#include <string>
#include "image.h"
using namespace std;

Image readData(string file){
    ifstream ifs;
    ifs.open(file,ios_base::binary);

    Image::Header h;

    ifs.read(&h.idLength,sizeof(h.idLength));
    ifs.read(&h.colorMapType,sizeof(h.colorMapType));
    ifs.read(&h.dataTypeCode,sizeof(h.dataTypeCode));
    ifs.read((char*)&h.colorMapOrigin,sizeof(h.colorMapOrigin));
    ifs.read((char*)&h.colorMapLength,sizeof(h.colorMapLength));
    ifs.read(&h.colorMapDepth,sizeof(h.colorMapDepth));
    ifs.read((char*)&h.xOrigin,sizeof(h.xOrigin));
    ifs.read((char*)&h.yOrigin,sizeof(h.yOrigin));
    ifs.read((char*)&h.width,sizeof(h.width));
    ifs.read((char*)&h.height,sizeof(h.height));
    ifs.read(&h.bitsPerPixel,sizeof(h.bitsPerPixel));
    ifs.read(&h.imageDescriptor,sizeof(h.imageDescriptor));

    Image img = Image(h);

    for(int i=0; i<h.width*h.height; i++){
        Image::Pixel p;
        ifs.read((char*)&p.b,sizeof(p.b));
        ifs.read((char*)&p.g,sizeof(p.g));
        ifs.read((char*)&p.r,sizeof(p.r));
        img.add(p);
    }

    ifs.close();
    return img;
}

void writeData(string file, Image& img){
    ofstream ofs;
    ofs.open(file,ios_base::binary);

    Image::Header h = img.getHeader();

    ofs.write(&h.idLength,sizeof(h.idLength));
    ofs.write(&h.colorMapType,sizeof(h.colorMapType));
    ofs.write(&h.dataTypeCode,sizeof(h.dataTypeCode));
    ofs.write((char*)&h.colorMapOrigin,sizeof(h.colorMapOrigin));
    ofs.write((char*)&h.colorMapLength,sizeof(h.colorMapLength));
    ofs.write(&h.colorMapDepth,sizeof(h.colorMapDepth));
    ofs.write((char*)&h.xOrigin,sizeof(h.xOrigin));
    ofs.write((char*)&h.yOrigin,sizeof(h.yOrigin));
    ofs.write((char*)&h.width,sizeof(h.width));
    ofs.write((char*)&h.height,sizeof(h.height));
    ofs.write(&h.bitsPerPixel,sizeof(h.bitsPerPixel));
    ofs.write(&h.imageDescriptor,sizeof(h.imageDescriptor));

    for(int i=0; i<img.length(); i++){
        ofs.write((char*)&(img[i].b),sizeof(img[i].get(2)));
        ofs.write((char*)&(img[i].g),sizeof(img[i].get(1)));
        ofs.write((char*)&(img[i].r),sizeof(img[i].get(0)));
    }
    ofs.close();
}
void Test(int i){
    if(i == 0){
        cout<<"Executing Task#1.../";
        Image i1 = readData("./input/layer1.tga");
        Image i2 = readData("./input/pattern1.tga");
        Image i3 = Image::Multiply(i1,i2);
        Image i4 = readData("./examples/EXAMPLE_part1.tga");
        writeData("./output/part1.tga",i3);
        cout<<"...";
        if(i3==i4){
            cout<<"Success :)"<<endl;
        }
        else{
            cout<<"Fail :("<<endl;
        }
    }
    else if(i == 1){
        cout<<"Executing Task#2.../";
        Image i1 = readData("./input/layer2.tga");
        Image i2 = readData("./input/car.tga");
        Image i3 = readData("./examples/EXAMPLE_part2.tga");
        Image i4 = Image::Subtract(i1,i2); 
        writeData("./output/part2.tga",i4);
        cout<<"...";
        if(i3==i4){
            cout<<"Success :)"<<endl;
        }
        else{
            cout<<"Fail :("<<endl;
        }
    }
    else if(i == 2){
        cout<<"Executing Task#3.../";
        Image i1 = readData("./input/layer1.tga");
        Image i2 = readData("./input/pattern2.tga");
        Image i3 = readData("./input/text.tga");
        Image i4 = readData("./examples/EXAMPLE_part3.tga");
        Image i5 = Image::Multiply(i1,i2);
        Image i6 = Image::Screen(i3,i5);
        writeData("./output/part3.tga",i6);
        cout<<"...";
        if(i4 == i6){
            cout<<"Success :)"<<endl;
        }
        else{
            cout<<"Fail :("<<endl;
        }
    }
    else if(i == 3){
        cout<<"Executing Task#4.../";
        Image i1 = readData("./input/layer2.tga");
        Image i2 = readData("./input/circles.tga");
        Image i3 = readData("./input/pattern2.tga");
        Image i4 = readData("./examples/EXAMPLE_part4.tga");
        Image i5 = Image::Multiply(i1,i2);
        Image i6 = Image::Subtract(i3,i5);
        writeData("./output/part4.tga",i6);
        cout<<"...";
        if(i4==i6){
            cout<<"Success :)"<<endl;
        }
        else{
            cout<<"Fail :("<<endl;
        }
    }
    else if(i == 4){
        cout<<"Executing Task#5.../";
        Image i1 = readData("./input/layer1.tga");
        Image i2 = readData("./input/pattern1.tga");
        Image i3 = readData("./examples/EXAMPLE_part5.tga");
        Image i4 = Image::Overlay(i1,i2);
        writeData("./output/part5.tga",i4);
        cout<<"...";
        if(i3==i4){
            cout<<"Success :)"<<endl;
        }
        else{
            cout<<"Fail :("<<endl;
        }
    }
    else if(i == 5){
        cout<<"Executing Task#6.../";
        Image i1 = readData("./input/car.tga");
        Image i2 = readData("./examples/EXAMPLE_part6.tga");
        Image i3 = Image::AddColor(i1,0,200,0);
        writeData("./output/part6.tga",i2);
        cout<<"...";
        if(i2==i3){
            cout<<"Success :)"<<endl;
        }
        else{
            cout<<"Fail :("<<endl;
        }
    }
    else if(i == 6){ 
        cout<<"Executing Task#7.../";
        Image i1 = readData("./input/car.tga");
        Image i2 = readData("./examples/EXAMPLE_part7.tga");
        Image i3 = Image::Scale(i1,4,1,0);
        writeData("./output/part7.tga",i3);
        cout<<"...";
        if(i2==i3){
            cout<<"Success :)"<<endl;
        }
        else{
            cout<<"Fail :("<<endl;
        }
    }
    else if(i == 7){
        cout<<"Executing Task#8.../";
        Image i1 = readData("./input/car.tga");
        Image i2 = readData("./examples/EXAMPLE_part8_r.tga");
        Image i3 = readData("./examples/EXAMPLE_part8_g.tga");
        Image i4 = readData("./examples/EXAMPLE_part8_b.tga");
        vector<Image> colors = Image::Seperate(i1);
        writeData("./output/part8_r.tga",colors[0]);
        writeData("./output/part8_g.tga",colors[1]);
        writeData("./output/part8_b.tga",colors[2]);
        cout<<"...";
        if(colors[0]==i2 && colors[1]==i3 && colors[2]==i4){
            cout<<"Success :)"<<endl;
        }
        else{
            cout<<"Fail :("<<endl;
        }
    }
    else if(i == 8){
        cout<<"Executing Task#9.../";
        Image i1 = readData("./input/layer_red.tga");
        Image i2 = readData("./input/layer_green.tga");
        Image i3 = readData("./input/layer_blue.tga");
        Image i4 = readData("./examples/EXAMPLE_part9.tga");
        Image i5 = Image::ColorCombine(i1,i2,i3);
        writeData("./output/part9.tga",i5);
        cout<<"...";
        if(i4==i5){
            cout<<"Success :)"<<endl;
        }
        else{
            cout<<"Fail :("<<endl;
        }
    }
    else if(i == 9){
        cout<<"Executing Task#10.../";
        Image i1 = readData("./input/text2.tga");
        Image i2 = Image::Flip(i1);
        Image i3 = readData("./examples/EXAMPLE_part10.tga");
        writeData("./output/part10.tga",i2);
        cout<<"...";
        if(i2==i3){
            cout<<"Success :)"<<endl;
        }
        else{
            cout<<"Fail :("<<endl;
        }
    }
    else if(i == 10){
        cout<<"Executing Extracredit.../";
        Image i1 = readData("./input/car.tga");
        Image i2 = readData("./input/circles.tga");
        Image i3 = readData("./input/pattern1.tga");
        Image i4 = readData("./input/text.tga");
        Image i5 = readData("./examples/EXAMPLE_extracredit.tga");
        Image i6 = Image::Combine(i1,i2,i3,i4);
        writeData("./output/extracredit.tga",i6);
        cout<<"...";
        if(i5==i6){
            cout<<"Success :)"<<endl;
        }
        else{
            cout<<"Fail :("<<endl;
        }
    }
}
int main(){
    for(int i=0; i<11; i++){
        Test(i);
    }
    return 0;
}
