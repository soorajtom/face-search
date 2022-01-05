import React from 'react';
import PropTypes from 'prop-types';
import styles from './Search.scss';

const Search = props => (
	<div>This is a component called Search.</div>
);

// todo: Unless you need to use lifecycle methods or local state,
// write your component in functional form as above and delete
// this section. 
// class Search extends React.Component {
//   render() {
//     return <div>This is a component called Search.</div>;
//   }
// }

const SearchPropTypes = {
	// always use prop types!
};

Search.propTypes = SearchPropTypes;

export default Search;
