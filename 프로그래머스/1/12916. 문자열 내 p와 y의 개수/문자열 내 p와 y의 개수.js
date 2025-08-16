function solution(s){
    var answer = true;

    let count1 = 0;
    let count2 = 0;
    let count3 = 0;
    for(let i=0;i<s.length;i++){
        if(s[i]=='p' || s[i]==='P'){
            count1++;
        }
        else if(s[i]=='y'||s[i]=='Y'){
            count2++;
        }
        else
            count3++;
    }
    
    if(count1==count2)
        return answer;
    else if(count3==s.lenght)
        return !answer;
    else
        return !answer;

}