import React from 'react';
import { shallow, render, mount } from 'enzyme';
import Search from './Search';

describe('Search', () => {
  let props;
  let shallowSearch;
  let renderedSearch;
  let mountedSearch;

  const shallowTestComponent = () => {
    if (!shallowSearch) {
      shallowSearch = shallow(<Search {...props} />);
    }
    return shallowSearch;
  };

  const renderTestComponent = () => {
    if (!renderedSearch) {
      renderedSearch = render(<Search {...props} />);
    }
    return renderedSearch;
  };

  const mountTestComponent = () => {
    if (!mountedSearch) {
      mountedSearch = mount(<Search {...props} />);
    }
    return mountedSearch;
  };  

  beforeEach(() => {
    props = {};
    shallowSearch = undefined;
    renderedSearch = undefined;
    mountedSearch = undefined;
  });

  // Shallow / unit tests begin here
 
  // Render / mount / integration tests begin here
  
});
