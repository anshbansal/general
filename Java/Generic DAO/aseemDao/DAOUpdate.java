package aseemDao;

import java.sql.Connection;
import java.sql.SQLException;

import aseemEnums.TableName;

public interface DAOUpdate {
	public abstract <T> boolean putInto(Connection con, TableName tableName,
			T oldPojo, T currentPojo) throws SQLException;
}
