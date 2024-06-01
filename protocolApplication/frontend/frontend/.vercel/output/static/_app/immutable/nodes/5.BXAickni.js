import{s as f,n as c}from"../chunks/scheduler.CvSFXg4c.js";import{S as g,i as v,e as d,c as l,d as b,g as C,f as u,h as S,j as _,k as y,l as T,p as $}from"../chunks/index.ClWzMdZj.js";function x(i){let t,e,n='<button class="btn btn-sm btn-primary mt-3 custom-btn" type="submit">Fetch all the calorie consumption details at all the dates</button><br/><br/> <div class="p-3 mb-2 bg-light text-dark rounded shadow-sm"><div id="content"></div></div>',o,r;return{c(){t=d("centre"),e=d("form"),e.innerHTML=n,this.h()},l(a){t=l(a,"CENTRE",{});var s=b(t);e=l(s,"FORM",{align:!0,"data-svelte-h":!0}),C(e)!=="svelte-1dnyj07"&&(e.innerHTML=n),s.forEach(u),this.h()},h(){S(e,"align","center")},m(a,s){_(a,t,s),y(t,e),o||(r=T(e,"submit",$(w)),o=!0)},p:c,i:c,o:c,d(a){a&&u(t),o=!1,r()}}}async function w(){let t=await(await fetch("http://localhost:8000/RetrieveCalorieDetails/",{method:"GET",credentials:"include"})).json();console.log(t),t.calorie_detail_retrieved.forEach(e=>{const n=new Date(e.currentdate),o=String(n.getUTCDate()).padStart(2,"0"),r=String(n.getUTCMonth()+1).padStart(2,"0"),a=n.getUTCFullYear(),s=String(n.getUTCHours()).padStart(2,"0"),m=String(n.getUTCMinutes()).padStart(2,"0"),p=String(n.getUTCSeconds()).padStart(2,"0"),h=`${o}/${r}/${a} ${s}:${m}:${p}`;document.getElementById("content").innerHTML+=`
                <div class="card w-100 h-100">
                    <div class="card-body d-flex flex-column justify-content-between gap-4">
                        <div>
                            <p class="card-text">Amount of Calories Consumed: ${e.amountofcalories} Kcal</p>
                            <p class="card-text">Date of the Calories Consumed: ${h}</p>
                        </div>
                    </div>
                </div>
            `})}function E(i){return[]}class D extends g{constructor(t){super(),v(this,t,E,x,f,{})}}export{D as component};
