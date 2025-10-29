//jacks code
int romanToInt(char *s) 
{
    int num=0;
    for(int i=0;i<strlen(s);i++)
    {
        switch(s[i])
        {
            case 'M':num+=1000;break;
            case 'D':num+=500;break;
            case 'C':
            if(s[i+1]=='D')
            {num+=400; i++;}
            else if(s[i+1]=='M')
            {num+=900; i++;}
            else
            num+=100;break;
            case 'L':num+=50;break;
            case 'X':
            if(s[i+1]=='L')
            {num+=40;i++;}
            else if(s[i+1]=='C')
            {num+=90;i++;}
            else
            num+=10;break;
            case 'V':num+=5;break;
            case 'I':
            if(s[i+1]=='V')
            {num+=4;i++;}
            else if(s[i+1]=='X')
            {num+=9;i++;}
            else
            num+=1;break;
            default: printf("Invalid");break;
        }   
    }
    return num;
}
//best code
int romanToInt(char* s) {
    int values[26];
    values['I' - 'A'] = 1;
    values['V' - 'A'] = 5;
    values['X' - 'A'] = 10;
    values['L' - 'A'] = 50;
    values['C' - 'A'] = 100;
    values['D' - 'A'] = 500;
    values['M' - 'A'] = 1000;

    int total = 0;
    int index = 0;
    for(int i= strlen(s) - 1; i >= 0; i--){
        int curr_values = values[s[i] - 'A'];
        if(curr_values<index){
            total -= curr_values;
        }else{
            total += curr_values;
        }
        index = curr_values;
    }
    return total;

}