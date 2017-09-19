import {
  JupyterLabPlugin
} from '@jupyterlab/application';

/**
 * Initialization data for the jupyterlab_hdf extension.
 */
const extension: JupyterLabPlugin<void> = {
  id: 'jupyterlab_hdf',
  autoStart: true,
  activate: (app) => {
    console.log('JupyterLab extension jupyterlab_hdf is activated!');
  }
};

export default extension;
