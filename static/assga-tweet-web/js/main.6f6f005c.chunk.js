(this["webpackJsonpassga-web"]=this["webpackJsonpassga-web"]||[]).push([[0],[,,,,,,,function(e,t,a){e.exports=a.p+"static/media/logo.5d5d9eef.svg"},function(e,t,a){e.exports=a(15)},,,,,function(e,t,a){},function(e,t,a){},function(e,t,a){"use strict";a.r(t);var n=a(0),c=a.n(n),r=a(4),l=a.n(r),o=(a(13),a(7)),s=a.n(o),i=(a(14),a(5)),m=a(1);function u(e){var t=c.a.createRef(),a=Object(n.useState)([]),r=Object(m.a)(a,2),l=r[0],o=r[1];return c.a.createElement("div",{className:e.className},c.a.createElement("div",{className:"col-12"},c.a.createElement("form",{onSubmit:function(e){e.preventDefault();var a=t.current.value,n=Object(i.a)(l);n.unshift({content:a,likes:0,id:1234}),o(n),t.current.value=""}},c.a.createElement("textarea",{ref:t,className:"form-control",required:!0,placeholder:"Tape ton tweet ici !"}),c.a.createElement("button",{type:"submit",className:"btn btn-primary my-3"}," Tweet "))),c.a.createElement(p,{newTweets:l}))}function p(e){var t=Object(n.useState)([]),a=Object(m.a)(t,2),r=a[0],l=a[1],o=Object(n.useState)([]),s=Object(m.a)(o,2),u=s[0],p=s[1];return Object(n.useEffect)((function(){var t=Object(i.a)(e.newTweets).concat(r);t.length!==u.length&&p(t)}),[e.newTweets,u,r]),Object(n.useEffect)((function(){!function(e){var t=new XMLHttpRequest;t.responseType="json",t.open("GET","http://localhost:8000/tweets/api/all"),t.onload=function(){e(t.response,t.status)},t.onerror=function(t){console.log(t),e({message:"The request was an error"},400)},t.send()}((function(e,t){200===t?l(e):alert("There was an error")}))}),[r]),u.map((function(e,t){return c.a.createElement(f,{tweet:e,className:"my-5 py-5 border bg-white text-dark",key:"".concat(t,"-{item.id}")})}))}function d(e){var t=e.tweet,a=e.action,r=Object(n.useState)(t.likes?t.likes:0),l=Object(m.a)(r,2),o=l[0],s=l[1],i=Object(n.useState)(!0===t.userLike),u=Object(m.a)(i,2),p=u[0],d=u[1],f=e.className?e.className:"btn btn-primary btn-sm",b=a.display?a.display:"Action",E="like"===a.type?"".concat(o," ").concat(a.display):b;return c.a.createElement("button",{className:f,onClick:function(e){e.preventDefault(),"like"===a.type&&(!0===p?(s(o-1),d(!1)):(s(o+1),d(!0)))}},E)}function f(e){var t=e.tweet,a=e.className?e.className:"col-10 mx-auto col-md-6";return c.a.createElement("div",{className:a},c.a.createElement("p",null,t.id," - ",t.content),c.a.createElement("div",{className:"btn btn-group"},c.a.createElement(d,{tweet:t,action:{type:"like",display:"Likes"}}),c.a.createElement(d,{tweet:t,action:{type:"unlike",display:"Unlike"}}),c.a.createElement(d,{tweet:t,action:{type:"retweet",display:""}})))}var b=function(){return c.a.createElement("div",{className:"App"},c.a.createElement("header",{className:"App-header"},c.a.createElement("img",{src:s.a,className:"App-logo",alt:"logo"}),c.a.createElement("p",null,"Edit ",c.a.createElement("code",null,"src/App.js")," and save to reload."),c.a.createElement("div",null,c.a.createElement(u,null)),c.a.createElement("a",{className:"App-link",href:"https://reactjs.org",target:"_blank",rel:"noopener noreferrer"},"Learn React")))};Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));var E=document.getElementById("root");E&&l.a.render(c.a.createElement(c.a.StrictMode,null,c.a.createElement(b,null)),E);var w=document.getElementById("tweetme-2");w&&l.a.render(c.a.createElement(c.a.StrictMode,null,c.a.createElement(u,null)),w),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then((function(e){e.unregister()})).catch((function(e){console.error(e.message)}))}],[[8,1,2]]]);
//# sourceMappingURL=main.6f6f005c.chunk.js.map