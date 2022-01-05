import React from 'react';
import PropTypes from 'prop-types';
import styles from './Login.scss';

const Login = props => (
	<div>This is a component called Login.</div>
);

// todo: Unless you need to use lifecycle methods or local state,
// write your component in functional form as above and delete
// this section. 
// class Login extends React.Component {
//   render() {
//     return <div>This is a component called Login.</div>;
//   }
// }

const LoginPropTypes = {
	// always use prop types!
};

Login.propTypes = LoginPropTypes;

export default Login;
