"use strict";

var React = require('react');
var Router = require('react-router');
var Link = Router.Link;
var RegisterForm=require('./RegisterForm');


var Register = React.createClass({
	render: function() {
		//noinspection JSDuplicatedDeclaration
        var styles = {
		    fontSize: 17,
            width: "290px",
            height: "330px",
            color : "#FFFFFF"

        };

		return (

            <center>
            <div className="Register Form" style={styles}>

				<RegisterForm/>
			</div>
             </center>
		);
	}
});



module.exports = Register;