package aseemDao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;

import aseemEnums.TableName;

public class OracleUpdate implements DAOUpdate {

	DAOFactory fac = null;

	OracleUpdate(DAOFactory fac) {
		this.fac = fac;
	}

	@Override
	public <T> boolean putInto(Connection con, TableName tableName, T oldPojo,
			T currentPojo) throws SQLException {
		PreparedStatement ps = null;
		try {
			ps = OracleSpecifics.<T> getPreparedUpdate(con, tableName, oldPojo,
					currentPojo);
			ps.execute();
		} finally {
			DAOFactory.closeAll(ps, null);
		}
		return true;
	}

}
