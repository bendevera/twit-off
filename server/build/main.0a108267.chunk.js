(this["webpackJsonptwit-off"]=this["webpackJsonptwit-off"]||[]).push([[0],{13:function(e,t,n){},14:function(e,t,n){},15:function(e,t,n){"use strict";n.r(t);var a=n(0),o=n.n(a),i=n(7),c=n.n(i),r=(n(13),n(1)),s=n(2),l=n(4),u=n(3),m=n(5),d=function(e){return o.a.createElement("nav",{className:"navbar navbar-dark bg-dark"},o.a.createElement("span",{className:"navbar-brand"},"twit off."))},h=function(e){return o.a.createElement("ul",{className:"list-group"},e.users.map((function(t){return t.id===e.id_one||t.id===e.id_two?o.a.createElement("li",{key:t.id,className:"list-group-item list-group-item-action list-group-item-info"},t.name):o.a.createElement("li",{key:t.id,value:t.id,onClick:e.makeActive,className:"list-group-item list-group-item-action"},t.name)})))},f=function(e){function t(e){var n;return Object(r.a)(this,t),(n=Object(l.a)(this,Object(u.a)(t).call(this,e))).handleChange=function(e){n.setState({screen_name:e.target.value})},n.handleAdd=function(e){e.preventDefault(),console.log(n.state.screen_name),n.props.sendUser(n.state.screen_name)},n.state={screen_name:""},n}return Object(m.a)(t,e),Object(s.a)(t,[{key:"render",value:function(){return o.a.createElement("form",{className:"form-inline justify-content-between my-2"},o.a.createElement("div",{className:"form-group mb-3 mx-1"},o.a.createElement("label",{className:"sr-only"},"Twitter Handle"),o.a.createElement("input",{onChange:this.handleChange,type:"text",className:"form-control",placeholder:"Twitter Handle"})),o.a.createElement("button",{onClick:this.handleAdd,className:"btn btn-outline-info mb-3 mx-1"},"add user"))}}]),t}(o.a.Component),p=function(e){function t(e){var n;return Object(r.a)(this,t),(n=Object(l.a)(this,Object(u.a)(t).call(this,e))).handleChange=function(e){n.setState({input:e.target.value})},n.handleSubmit=function(e){e.preventDefault(),n.props.makePrediction(n.state.input)},n.state={input:""},n}return Object(m.a)(t,e),Object(s.a)(t,[{key:"render",value:function(){var e;return e=this.props.prediction?o.a.createElement("h2",{className:"text-dark my-2"},"That has to be ",this.props.prediction,"!"):o.a.createElement("div",null),o.a.createElement("div",null,o.a.createElement("div",{className:"form-group"},o.a.createElement("label",null,"example tweet"),o.a.createElement("textarea",{className:"form-control",rows:"3",onChange:this.handleChange})),o.a.createElement("button",{onClick:this.handleSubmit,className:"btn btn-outline-info"},"get prediction"),e)}}]),t}(o.a.Component),b="https://twit-off-bendevera.herokuapp.com",v=(n(14),function(e){function t(e){var n;return Object(r.a)(this,t),(n=Object(l.a)(this,Object(u.a)(t).call(this,e))).addUser=function(e){(function(e){return new Promise((function(t,n){console.log(b+"/api/users"),fetch(b+"/api/users",{method:"POST",headers:{Accept:"application/json","Content-Type":"application/json"},body:JSON.stringify({screen_name:e})}).then((function(e){return e.json()})).then((function(e){t(e.data)})).catch((function(e){n(e)}))}))})(e).then((function(e){console.log(e)}))},n.makeActive=function(e){n.setState({id_one:e.target.value,id_two:n.state.id_one})},n.makePrediction=function(e){var t,a,o;(t=n.state.id_one,a=n.state.id_two,o=e,new Promise((function(e,n){console.log(b+"/api/predict"),fetch(b+"/api/predict",{method:"POST",headers:{Accept:"application/json","Content-Type":"application/json"},body:JSON.stringify({id_one:t,id_two:a,sentence:o})}).then((function(e){return e.json()})).then((function(t){e(t.data)})).catch((function(e){n(e)}))}))).then((function(e){console.log(e),n.setState({prediction:e})})).catch((function(e){console.log(e)}))},n.state={users:[],id_one:null,id_two:null,prediction:null},n}return Object(m.a)(t,e),Object(s.a)(t,[{key:"componentDidMount",value:function(){var e=this;new Promise((function(e,t){console.log(b+"/api/users"),fetch(b+"/api/users").then((function(e){return e.json()})).then((function(t){e(t.data)})).catch((function(e){t(e)}))})).then((function(t){console.log(t),e.setState({users:t})})).catch((function(e){console.log("ERROR:"),console.log(e)}))}},{key:"render",value:function(){return o.a.createElement("div",{className:"App bg-light vh-100"},o.a.createElement(d,null),o.a.createElement("div",{className:"row mx-1"},o.a.createElement("div",{className:"col"},o.a.createElement(f,{sendUser:this.addUser}),o.a.createElement(h,{users:this.state.users,id_one:this.state.id_one,id_two:this.state.id_two,makeActive:this.makeActive})),o.a.createElement("div",{className:"col"},o.a.createElement(p,{makePrediction:this.makePrediction,prediction:this.state.prediction}))))}}]),t}(o.a.Component));Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));c.a.render(o.a.createElement(v,null),document.getElementById("root")),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then((function(e){e.unregister()})).catch((function(e){console.error(e.message)}))},8:function(e,t,n){e.exports=n(15)}},[[8,1,2]]]);
//# sourceMappingURL=main.0a108267.chunk.js.map