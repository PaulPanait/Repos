/**
 * Created by Pauly on 22.07.2016.
 */
"use strict";

var React = require('react');
var Router = require('react-router');
var Link = Router.Link;

var LoginForm = React.createClass({
	render: function() {
        document.body.style.backgroundImage = "url('bla3.jpg')";
        document.body.style.backgroundPosition = "center center";
        return (
			<form>
                <h2>LOGIN</h2>
                <label htmlFor="Username">Username:</label>
                <input type="text" name="Username"
                className="form-control"
                placeholder="Username"
                ref="Username"
                />
                <br />

                <label htmlFor="Password">Password:</label>
                <input type="password"
                       name="Password"
                       className="form-control"
                       placeholder="Password"
                       ref="password"
                       />
                <br />

                 <Link to = "Login">
                    <input type="button" value = "Login"/>
                    </Link>


                <Link to = "Register">
                     <label htmlFor="Register">If you don't have account register here</label>
                    </Link>
            </form>

		);
	}
});

module.exports = LoginForm;