function solution(n) {
    let str=n+"";
    let arr=[];
    arr=str.split("");
    let max;
    for(let i=0;i<str.length-1;i++){
        max=i;
        for(let j=i+1;j<str.length;j++){
            if(arr[max]<arr[j])
                max=j;
        }
        temp=arr[i];
        arr[i]=arr[max];
        arr[max]=temp;    
    }
    
    let arr2="";
    for(let i=0;i<arr.length;i++)
        arr2=arr2+arr[i];
    
    return +arr2;
}

