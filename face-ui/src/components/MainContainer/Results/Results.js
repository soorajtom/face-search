import React from 'react';
import PropTypes from 'prop-types';
import styles from './Results.scss';

const Results = props => (
	<div>This is a component called Results.</div>
);

// todo: Unless you need to use lifecycle methods or local state,
// write your component in functional form as above and delete
// this section. 
// class Results extends React.Component {
//   render() {
//     return <div>This is a component called Results.</div>;
//   }
// }

const ResultsPropTypes = {
	// always use prop types!
};

Results.propTypes = ResultsPropTypes;

export default Results;
