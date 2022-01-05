import React from 'react';
import PropTypes from 'prop-types';
import styles from './MainContainer.scss';
import Login from './Login';
import Search from './Search';
import { Container, Header } from 'semantic-ui-react';

// const MainContainer = props => (
// 	<div>This is a component called MainContainer.</div>
// );

// todo: Unless you need to use lifecycle methods or local state,
// write your component in functional form as above and delete
// this section. 
class MainContainer extends React.Component {
	constructor(props) {
		super(props);
		this.state = {auth: false};
	}
	handleSuccessfulLogin(){
		this.setState({
			auth: true
		  })
	}
	render() {
		if (!this.state.auth){
			return(
				<Container text>
					<Login handleSuccessfulLogin = {this.handleSuccessfulLogin.bind(this)} />
				</Container>
			);
		} else {
			return(
				<Container text>
					<Search/>
				</Container>
			);
		}
	}
}

const MainContainerPropTypes = {
	// always use prop types!
};

MainContainer.propTypes = MainContainerPropTypes;

export default MainContainer;
